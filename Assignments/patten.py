import re

mystr="This is Python"

#x=re.match('This',mystr)
#x=re.search('This',mystr)
x=re.findall('is',mystr)
print(x)