fl=open("stdata.txt","a")

id=input("Enter ID:")
name=input("Enter Name:")

fl.write(f"Student ID:{id}\nStudent Name:{name}\n")