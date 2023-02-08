import pytest


def add(x, y):
    return x + y


@pytest.mark.parametrize('value1,value2,expected_result',
                         [(4, 5, 9), (40.5, 59.5, 100.0), ("chandan", "mishra", "chandanmishra"),("","","null"),(4,"chandan","4chandan")])
def test_add(value1, value2, expected_result):
    try:
        assert add(value1, value2) == expected_result
    except Exception as e:
        assert str(e)=="unsupported operand type(s) for +: 'int' and 'str'"


