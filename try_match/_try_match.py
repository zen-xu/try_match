
try:
    from collections.abc import Container
except ImportError:
    from collections import Container

import inspect
import sys

class _Base(Exception):
    pass


DefaultCase = Exception


def match(value):
    class _Match(_Base):
        pass

    _Match.value = value
    raise _Match("match nothing")


def Case(case):
    """
    case can be value, class, range, lambda
    """

    class _Case(_Base):
        pass

    match_cls, _, _ = sys.exc_info()
    value = getattr(match_cls, "value", None)

    if value:
        matched = False

        if inspect.isclass(case) and isinstance(value, case):
            matched = True

        elif callable(case) and not inspect.isclass(case):
            matched = case(value)

        elif not isinstance(case, Container):
            matched = value == case

        elif isinstance(case, Container) and isinstance(case, str):
            matched = value == case

        elif isinstance(case, Container) and not isinstance(case, str):
            matched = value in case

        if matched:
            match_cls.__bases__ = (_Case,)

    return _Case