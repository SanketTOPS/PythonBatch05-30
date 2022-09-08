fl=open('myfile.txt','w')

#fl.write("Hello Student!")

id=input("Enter your ID:")
name=input("Enter your Name:")

fl.write(f"Student ID:{id}")
fl.write(f"Student Name:{name}")
