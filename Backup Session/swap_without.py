a=34
b=67

"""temp=a 
a=b
b=temp"""

a, b = b, a

"""a=a+b
b=a-b
a=a-b
"""
print("A:",a)
print("B:",b)