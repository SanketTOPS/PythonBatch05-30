"""fl=open('stdata.txt','r')
#print(fl.read())
#print(fl.readlines()[2])"""


import random

"""fl=open('stdata.txt').read().splitlines()
ranline=random.choice(fl)
print(ranline)"""

myline=random.choice(open('stdata.txt').readlines())
print(myline)
