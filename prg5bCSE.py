import re
phone_pat=re.compile(r'\+\d{12}$')
email_pat=re.compile(r'[0-9a-zA-Z._]+@gmail.com')
f=open("example.txt",'r')
for line in f:
    matches=phone_pat.findall(line)
    for match in matches:
        print(match)
    matches=email_pat.findall(line)
    for match in matches:
        print(match)