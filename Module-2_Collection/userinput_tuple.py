mylist=[]

n=int(input("How many elements you want for list?:"))

for i in range(n):
    el=input("Enter list element:")
    mylist.append(el)

print(tuple(mylist))
