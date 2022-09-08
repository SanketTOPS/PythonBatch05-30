strlist=['saw','aba','xyz','abc','2152']

#print(len(strlist))

cn=0
for i in strlist:
    if len(i)>1 and i[0]==i[-1]:
        cn+=1

print(cn)

