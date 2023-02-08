import pytest
#pytest.skip(allow_module_level=True,reason="not working due to changes")

name = "chandan"


@pytest.mark.unit
@pytest.mark.skip(reason="obsolute test")
def test_len_function():
    assert len(name) == 7


@pytest.mark.smoke
def test_slice_string():
    assert name[2:len(name)] == 'chandan'


def test_string_contains():
    full_name = "my name is chandan"
    result = name in full_name
    assert result == True


@pytest.mark.critical
def test_ends_with():
    pdf_url = 'https://calibre-ebook.com/downloads/demos/demo.docx'
    assert pdf_url.endswith(".docx") == True


@pytest.mark.high
@pytest.mark.order(1)
def test_list_slice_ends():
    list1 = ['a', 'b', 'c']

    my_name = "chandan"
    output = my_name[::-1]
    assert output == 'chandan'


@pytest.mark.critical
@pytest.mark.smoke
@pytest.mark.stage_only
def test_dictionary_access_items():
    my_dictionary = {"name": "chandan", "age": 30}

    # access dictionary
    assert my_dictionary['name'] == 'chandan'

