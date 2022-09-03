def checklist(mylist, sublist):
    x=False
    if sublist == mylist:
        x=True
    elif len(sublist) > len(mylist):
        x=False
    else:
        for i in range(len(mylist)):
            if mylist[i]==sublist[0]:
                cn=1
                while(cn<len(sublist) and (mylist[i+cn]==sublist[cn])):
                    cn+=1
                    print(cn)
                if cn==len(sublist):
                    x=True
    return x

ls=[3,7,1,8,4]
sl=[1,8]

print(checklist(ls,sl))
