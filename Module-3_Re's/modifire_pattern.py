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
#x=re.findall('\w',mystr) #word
#x=re.findall('\W',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\Athis',mystr)
#x=re.findall(r'\bThis',mystr)
#x=re.findall('\B77',mystr)
#x=re.findall('\s',mystr)
#x=re.findall('\S',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('Py..on',mystr)
#x=re.findall('This|That',mystr)
x=re.findall('[A-Z]|[a-z]',mystr)
print(x)

if x:
    print("Pattern match done....")
else:
    print("Error!")