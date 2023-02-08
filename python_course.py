print("test")

tup = ("alla", "bella", "charlie")
print(tup[0])
list1=[1,2,3,4,5,6,7,8,9,10]
list1.pop(0)

print(list1)

name="/n"
print(name+"a")
print(len(name))
print(name[2:len(name)])
full_name="my name is chandanchandan"
#contains demo
print(name[0:-3])
print(name in full_name)


# formatting

xpath = "select[contains(text()='{dropdown_value}' and input[@class='{class_name}']]"
print(xpath.format(dropdown_value="Delhi",class_name="textbox"))


pdf_url='https://site.com/document.pdf'
print(pdf_url.endswith(".pdf"))

name = "chandan"
name_list=['c','h','a','n','d','a','n']
# map=char,value, c=1 h=1 a=2 n=2 d=1 in sorted key order-- a=2 c=1 =1 h=1 n=2
output_dictionary = {}
for item in name:
    if not output_dictionary.keys().__contains__(item):
        output_dictionary[item]=1
    else:
        output_dictionary[item]=output_dictionary[item]+1


print(output_dictionary)
print(dict(sorted(output_dictionary.items())))
print(sorted(output_dictionary.values()))


def sum(first_number, second_number):
    print("this is a test")
    return first_number+second_number


print(sum(4, 9))


def print_values(*args):
    return args


print(print_values("chandan"))

print(print_values("chandan"), 1)

print(print_values("chandan"), 989.7989)
print(print_values("chandan","chandan@123"))
print(print_values("chandan","chandan@123"))


def select_browser(browser_name="chrome"):
    print(browser_name)


print(select_browser())
print(select_browser("firefox"))


def handle_payloads(**payloads):
    result="user not found"
    if payloads['username']=="chandan":
        result="user is valid"
    else:
        result="invalid user"

    return result


print(handle_payloads(username='chandan', password="chandan@123", email="chandan@gmail.com"))

