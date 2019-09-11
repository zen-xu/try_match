from try_match import __version__, DefaultCase, Case, match


def test_version():
    assert __version__ == '0.1.1'


def test_int_value():
    try:
        match(1)
    except Case(2):
        raise AssertionError
    except Case('1'):
        raise AssertionError
    except Case(1):
        pass
    except Case(3):
        raise AssertionError
    except DefaultCase:
        raise AssertionError

def test_str_value():
    try:
        match('1')
    except Case('2'):
        raise AssertionError
    except Case(1):
        raise AssertionError
    except Case('1'):
        pass
    except Case('3'):
        raise AssertionError
    except DefaultCase:
        raise AssertionError


def test_non_built_in_type_value():
    class Value(object):
        def __init__(self, v1, v2):
            self.v1 = v1
            self.v2 = v2

        def __eq__(self, other):
            return (self.v1 == other.v1) and (self.v2 == other.v2)

    try:
        match(Value(1, 2))
    except Case(Value(2, 2)):
        raise AssertionError
    except Case(Value(2, 1)):
        raise AssertionError
    except Case(Value('1', 2)):
        raise AssertionError
    except Case(Value(1, '2')):
        raise AssertionError
    except Case(Value(1, 2)):
        pass
    except DefaultCase:
        raise AssertionError


def test_class():
    try:
        match(1)
    except Case(str):
        raise AssertionError
    except Case(int):
        pass
    except DefaultCase:
        raise AssertionError

def test_range():
    try:
        match(20)
    except Case(range(1, 10)):
        raise AssertionError
    except Case(range(1, 20)):
        raise AssertionError
    except Case(range(20, 100)):
        pass
    except DefaultCase:
        raise AssertionError


def test_lambda():
    try:
        match(20)
    except Case(lambda v: v > 21):
        raise AssertionError
    except Case(lambda v: v < 20):
        raise AssertionError
    except Case(lambda v: v <= 20):
        pass
    except DefaultCase:
        raise AssertionError

def test_default_case():
    try:
        match(0)
    except Case(1):
        raise AssertionError
    except Case(2):
        raise AssertionError
    except DefaultCase:
        pass
