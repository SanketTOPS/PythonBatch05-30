fl=open('stdata.txt','r+')

#print(fl.read())
#print(fl.readline())
#print(fl.readlines()[2])

#fl.write("\nHello")

n=1
for i in fl:
    #print(i)
   print(f"Line={n} : {i}")
   n+=1

fl.close()