n=int(input("Enter any number:"))

x=0 #start
y=1 #base 

for i in range(1,n):
    fib=x+y
    x=y
    y=fib
    print(fib)