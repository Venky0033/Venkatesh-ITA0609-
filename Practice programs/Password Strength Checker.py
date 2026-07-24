import re
pwd = input("Enter password: ")

if (len(pwd) >= 8 and re.search("[A-Z]", pwd) and re.search("[a-z]", pwd)
    and re.search("[0-9]", pwd) and re.search("[@#$%^&*!]", pwd)):
    print("Strong Password")
else:
    print("Weak Password")
