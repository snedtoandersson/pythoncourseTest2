import pytest


@pytest.fixture(scope='session', autouse=True)
def session_start():
    print("run this code before project")

    yield
    print("run this after project")


@pytest.fixture(scope='module', autouse=True)
def before_module_file():
    print("run this code before each module")

    yield
    print("run this code after module")


@pytest.fixture(scope='class', autouse=True)
def before_class_code():
    print("this is a code which will run before classes from conftest")

    yield
    print("this is a code which will run after classes from conftest")


@pytest.fixture(scope='function', autouse=True)
def before_method_file():
    print("run this code before method from conftest")
    print("test line 2")

    yield
    print("run this code after method from conftest")


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        choices=["dev", "qa", "prod"],
        help="these are the different env values to be provided from command line during test execution"

    )
    parser.addoption(
        "--thread_count",
        action="store",
        default="4",
        choices=["1","4", "2", "8"],
        help="thread count parameter is used to provide threadcount for thread polling during during thread creation"

    )


@pytest.fixture(scope="function")
def get_env_value(pytestconfig):
    return pytestconfig.getoption('env')


@pytest.fixture(scope="function")
def get_thread_count_value(pytestconfig):
    return pytestconfig.getoption('thread_count')