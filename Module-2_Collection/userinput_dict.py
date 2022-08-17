stdata={}

n=int(input("How many pairs you want for dict?:"))

for i in range(n):
    key=input("Enter Key:")
    value=input("Enter Value:")
    stdata[key]=value

print(stdata)