a="hello i am using python "
b="PYTHON"
c="43896"
print(type(a))
print(len(a))
if "he" in a:
   print("true he in a")
else:
   print("false")
if type(a) is str:
   print("yes a string value")
else:
   print("no a is not a string value")
print(a.isalpha(),"alpha value") # it is true only when alpha value only
print(b.isalpha(),"alpha value") # other wise false
print(c.isdigit(),"digit value") #it shows only when number is string digit only true
print(a.isspace())
print(a.islower(),"it is lowercase")
print(c.isalnum(),"it is alphanumeric value") # it is true for alphanumeric value or numeric
print(a.split("l"))
print(a.split())
d=b.rjust(45,"*")
print(d)
e=c.ljust(55,"/")
print(e)
f="kkkkkpython"
j=f.lstrip("k")
print(j)
o="ramaaaaaaaaaa"
k=o.rstrip("a")
print(k)
print(a.startswith("h"),"startswith")
print(a.endswith("n"),"endswith")
print(a.title())
