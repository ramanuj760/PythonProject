x={}
x["name"]="ramanuj"
x["age"]=20
x["rollno"]=50
x["marks"]=90
x["address"]="dwarka"
print(x)
print(x["name"])
print(x.get("number",86))
print(x)
x["x1"]=[1,2,4,8]
print(x)
y=x.copy()
z=dict.fromkeys(y)
print(z)
print(x)
print(x.items()) # everything in paranthesis tuple is collection collections

for items in x.items():
    print(items)
for keys in x.keys():
    print(keys)
for values in x.values():
    print(values)
x.setdefault("house","janta flat")# it does not overwrite it give new value if keys is same it doesnot give values
print(x)
#x2=("class":"python")
x.update({"class":"python"})
print(x)
x3=([("name","anuj"),("age","na")])
print(x)
"""def dict(a,b):
    a=4+5
    b=6+7
    return a,b
c={a:b}
d=dict(c)"""
x.pop("house")
print(x)
x.clear()
print(x)
l=[0,1,1,0,0,1]
print(any(l))
print(all(l))
