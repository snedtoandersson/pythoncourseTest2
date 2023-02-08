from enum import Enum


class Employee:
    def __init__(self, emp_id, emp_age, emp_name):
        self.emp_id = emp_id
        self.emp_age = emp_age
        self.emp_name = emp_name

    def print_emp_details(self):
        print(self.emp_id)
        print(self.emp_age)
        print(self.emp_name)


emp_object = Employee(1, 30, "chandan")
emp_object.print_emp_details()


class Employee2:
    test_variable = 5


print(Employee2.test_variable)


class BaseTest:
    def __init__(self,token):
        self.token=token


    def get_token(self):
        print(self.token)
        return self.token


class LoginTest(BaseTest):
    def print_token(self):
        super().get_token()


login_object=LoginTest("diuhishihih")
print(login_object.token)
print(login_object.get_token())
print(login_object.print_token())


class TestResult(Enum):
    PASS=1
    FAIL=2
    BlOCKED=3
    SKIPPED=4


print(TestResult.PASS.name)
print(TestResult.PASS.value)

try:
    name="chandan"
    print(name[10])
except Exception as e:
    print(e)

finally:
    print("clean objects")
