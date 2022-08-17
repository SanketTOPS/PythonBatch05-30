stdata={'id':1,'name':'sanket','sub':'python'}

"""print(stdata)
print(stdata["sub"])
print(stdata["name"])
print(stdata.get("id"))"""

#print(len(stdata))

print(stdata)
#print(stdata.keys())
#print(stdata.values())

"""if "name" in stdata:
    print("Yes...")
else:
    print("Nooo")"""

"""if "nirav" in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

#stdata["id"]=2
#print(stdata)

"""for i in stdata: #only keys
    print(i)"""

"""for i in stdata.values(): #only values
    print(i)"""

"""for i in stdata.items(): #key-value
    print(i)"""

# Key=id and Value=1
# Key=name and Value=sanket

"""for i in stdata:
    print(f"Key={i} and Value={stdata[i]}")"""

"""for i,j in stdata.items():
    print(f"Key={i} and Value={j}")"""

# ---------------------------------------- #

stdata["city"]="Rajkot"
#stdata.pop("name")
#del stdata['city']
#stdata.clear()
#del stdata
#print(stdata)

newdict=stdata.copy()
print(newdict)
