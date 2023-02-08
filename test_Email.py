import re



# Define a function for
# for validating an Email
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex, email):
        return True

    else:
       return False



def test_check():
    assert check("d@dsu.se")==True