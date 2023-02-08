import pytest


@pytest.fixture(scope='session', autouse=True)
def session_start():
    print("run this code before project")

    yield
    print("run this after project")


# @pytest.fixture(scope='module',autouse=True)
# def before_module_file():
#     print("run this code before each module")
#
#     yield
#     print("run this code after each module")

@pytest.fixture(scope='class', autouse=True)
def before_class_code():
    print("this is a code which will run before classes from conftest")

    yield
    print("this is a code which will run after classes from conftest")

