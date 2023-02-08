import pytest

# pytest.skip(allow_module_level=True,reason="not working due to changes")

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


a = 9


@pytest.mark.skipif(a==0,reason="0 is supported as denom")
def test_skip_if_for_divide():
    b = 5
    c = b / a
    print(c)


@pytest.mark.open_issues
@pytest.mark.xfail
def test_existing_issues():
    print("there is a open issue for this")
    assert 6 == 4