import re

mystr="This is Python!79878"

#x=re.findall('[A-Z]',mystr)
#x=re.findall('[a-z]',mystr)
#x=re.findall('[0-9]',mystr)
#x=re.findall('[A-Za-z]',mystr)
#x=re.findall('[A-Za-z0-9]',mystr)
#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('79$',mystr)
#x=re.findall('[^A-Z]',mystr)
#x=re.findall('[^A-Za-z0-9]',mystr)
#x=re.findall('\w',mystr)
x=re.findall('\W',mystr)
print(x)