import getpass


def get_local_user():
    return getpass.getuser()


def test_get_user(monkeypatch):
    def mock_getuser():
        return 'root'

    monkeypatch.setattr(getpass,"getuser",mock_getuser)

    print(get_local_user())

