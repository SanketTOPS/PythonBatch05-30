fl=open('test.txt','w')

fl.write("This is Python File.")
fl.write("\nHello Student")

if fl.writable():
    print("Yes...")
else:
    print("Error!")
