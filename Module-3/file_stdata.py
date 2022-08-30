fl=open("stdata.txt","a")

id=input("Enter ID:")
name=input("Enter Name:")
sub=input("Enter Subject:")

fl.write(f"\n{id}\n{name}\n{sub}\n")