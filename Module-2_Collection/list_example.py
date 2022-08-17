tech=["Python","Android","PHP","JAVA","NET"]

"""print(tech)
print(tech[0])
print(tech[-1])
print(tech[0:3]) #range
print(tech[2:])
print(tech[:4])"""

#print(len(tech))

"""if "Python" in tech:
    print("Yes...")
else:
    print("Nooo")
"""

#print(tech)
#tech[1]="iOS"
#print(tech)

"""for i in tech:
    print(i)"""

# Index[0]=Python
# Index[1]=Android

"""n=0
for i in tech:
    #print(i)
    print(f"Index[{n}]={i}")
    n+=1"""

"""print(tech.index("PHP"))
for i in tech:
    #print(i)
    print(f"Index[{tech.index(i)}]={i}")"""

# ---------------------------------------------- #

#print(tech)
tech.append("iOS")
tech.insert(2,"C++")
#tech.pop()
#tech.pop(1)
#tech.clear()
#del tech[2]
#del tech
#tech.sort()
#tech.reverse()
print(tech)

#newlist=tech.copy()
#print(newlist)

newlist=["Node","React","Angular"]

#print(tech+newlist)
tech.extend(newlist)
print(tech)


