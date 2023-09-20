import re

def isphoneNo(num):
    if (len(num) == 12 and
        num[0:3].isdigit() and
        num[4:7].isdigit() and
        num[9:12].isdigit() and
        num[3] == '-' and
        num[7] == '-'):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")

def checkphoneNo(num):
    pattern = r'\d{3}-\d{3}-\d{4}'
    result = re.match(pattern, num)
    if result:
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")

n = input("Enter Number\n")
print("Without Using Regular Expression")
isphoneNo(n)
print("Using Regular Expression")
res1 = checkphoneNo(n)
