import pytest


class TestClass1:
    def setup_class(self):
        print("i am in class before")

    def teardown_class(self):
        print("i am in the class after")

    def setup_method(self):
        print("before method")

    def teardown_method(self):
        print("after method")

    @pytest.mark.critical
    def test_class_method1_for_list_len(self):
        print("during method")
        list2 = [788, 34, 90, 1, 65]
        assert len(list2) == 5

    def test_class_method2_for_list_compare(self):
        list1 = [788, 34, 90, 1, 65]
        list2 = list1.sort()
        assert list2 == list1


class TestClass2:fixtures.py
    def test_method3_dict(self):
        my_dictionary = {"name": "chandan", "age": 30}
        assert my_dictionary.keys() == my_dictionary.values()

    def test_method_4_tuple(self):
        tup = ("chandan", "john", "ruby")
        assert len(tup) == 3

