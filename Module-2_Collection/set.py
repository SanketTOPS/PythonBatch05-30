myset={'A','B','C','D','E','F','A','B','D'}

#print(myset)
#print(myset[0])


#print(len(myset))

"""if "B" in myset:
    print("Yes...")
else:
    print("Noo")"""


"""for i in myset:
    print(i)"""

# --------------------------------------- #

#myset.add("P")
#myset.update(["Q","R","S","T"])
#myset.remove("R")
#myset.pop()
#myset.clear()
#del myset
#print(myset)

# ------------------------------------ #

newset={"X","Y","Z","A","D","F"}

print(myset)
print(newset)

#x=myset.union(newset)
x=myset.intersection(newset)
print(x)

