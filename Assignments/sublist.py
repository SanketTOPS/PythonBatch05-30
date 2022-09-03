
mylist=[2,3,5,1,56,34,67]
print(mylist)

sublist=[3,5,1]

for i in range(len(mylist)-len(sublist)+1):
    if mylist[i:i+len(sublist)]==sublist:
        print("Yes")

