if True:
    print("True")

if False:
    print("True")


if language == "Python":
    print('Python')
language = "Python"


# Comparison
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greate or Equal: >=
# Less or Equal: <=
# Object Identity: is

language = "java"

if language == "Python":
    print('Python')
else:
    print("Not python")

language = "CSS"

if language == "Python":
    print('Python')
elif language == "Java":
    print("Java")
else:
    print("Not Match")

# Boolean
# and
# or
# not

user = "Admin"
loggin_in = True

if user == "Admin" and loggin_in:
    print("user log in")
else:
    print("Not login")

user = "Admin User"
loggin_in = False

if user == "Admin" or loggin_in:
    print("user log in")
else:
    print("Not login")

if not False:
    print("not False")

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
c = a
print(c is a)
print(a == b)

# False Values:
# False
# None
# Zero of any numeric type
# any empty sequence for example "", (), []
# any empty mapping for example {}

condition = [1]

if condition:
    print("I am true")
else:
    print("Not True")