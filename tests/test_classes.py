import pytest


class TestClass1:
    @pytest.mark.critical
    def test_class_method1_for_list_len(self):
        list2 = [788, 34, 90, 1, 65]
        assert len(list2) == 5

    def test_class_method2_for_list_compare(self):
        list1 = [788, 34, 90, 1, 65]
        list2 = list1.sort()
        assert list2 == list1


class TestClass2:
    def test_method3_dict(self):
        my_dictionary = {"name": "chandan", "age": 30}
        assert my_dictionary.keys() == my_dictionary.values()

    def test_method_4_tuple(self):
        tup = ("chandan", "john", "ruby")
        assert len(tup) == 3
