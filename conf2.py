import pytest


def test_cmd_params_value(get_env_value, get_thread_count_value):
    print("test cmd param")
    print(get_env_value)
    print(get_thread_count_value)


@pytest.fixture
def get_value1():
    return 5


@pytest.fixture
def get_value2():
    return 10


@pytest.fixture
def get_sum():
    return 15


@pytest.mark.parametrize("input1,input2,result", [("get_value1", "get_value2", "get_sum")])
def test_fixtures_in_params(input1, input2, result, request):
    assert request.getfixturevalue(input1) + request.getfixturevalue(input2) == request.getfixturevalue(result)
