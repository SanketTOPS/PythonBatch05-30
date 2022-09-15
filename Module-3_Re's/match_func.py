import re

mystr="This is Python!"

x=re.match('is',mystr)
print(x)

if x:
    print("Yes...")
else:
    print("Error!")