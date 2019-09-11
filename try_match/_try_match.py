from abc import ABCMeta

import collections, inspect


class Meta(ABCMeta):
    def __subclasscheck__(cls, subclass):
        value = getattr(subclass, "value", None)
        case = getattr(cls, "case", None)
        if not (value and case):
            return False

        if inspect.isclass(case):
            return isinstance(value, case)
        elif callable(case):
            return case(value)
        elif not isinstance(case, collections.Iterable):
            return case == value
        elif isinstance(case, collections.Iterable):
            return value in case
        else:
            return False


class DefaultCase(Exception):
    __metaclass__ = ABCMeta


class ProxyException(Exception):
    __metaclass__ = ABCMeta


def match(value):
    class _Match(Exception):
        __metaclass__ = ABCMeta
    _Match.value = value
    ProxyException.register(_Match)
    DefaultCase.register(_Match)

    raise _Match


def Case(case):
    class _Case(Exception):
        __metaclass__ = Meta

    if callable(case):
        _Case.case = staticmethod(case)
    else:
        _Case.case = case
    _Case.register(ProxyException)

    return _Case