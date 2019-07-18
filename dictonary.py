a={}
print(a)
a["name"]="ramanuj"
print(a)
a['age']=20
print(a)
print(a.get("address"))
a.setdefault("address","dwarka")#key:value are added in dictonary
print(a)
b=a.copy()
print(b)
c=dict.fromkeys(a)#key are same but value are none
print(c)
print(a.values())#print values only of that key
d={"name":"anuj"}
a.update(d)
print(a)
ls=dict([("name","gupta"),("age","66")])#it give dictionary
print(ls)