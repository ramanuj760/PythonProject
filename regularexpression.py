# import re# regular expression
# message="call me 124-696-7587 tomarrow"\
# "or at 346-965-7549"
# X=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo=X.search(message)
# print(mo.group())
# print(X.findall(message),"findall")
# X=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo=X.search(message)
# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(3))
# message="call me (124) 696 7587 tomarrow"
# X=re.compile(r'(\d\d\d) \d\d\d \d\d\d\d')
# mo=X.search(message)
# print(mo.group())
# print(X.findall(message))
#
message=" call me 460-967-3769"\
            " or 751-369-4865 "
import re
MobilePhoneX=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
y=MobilePhoneX.search(message)
print(y.group())
print(MobilePhoneX.findall(message))
print(y.group(1))
print(y.group(2))
print(y.group(3))

for i in MobilePhoneX.findall(message):
    print(y.group())
print("pin with number")
print()

message=" call me (460) 967-3769,  or (751) 369-4865 "
MobilePhoneX=re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
y=MobilePhoneX.search(message)
print(y.group())
print(MobilePhoneX.findall(message))
print("#pipe character")
# batRegX=re.compile(r'Bat(man|mobile|copter|bat)')
# y=batRegX.search("Batman lost a wheel")
# print(y.group())
T=re.compile(r'Bat(man|ball|stamp|cricket)')
s=T.search("i am play Batball")
print(s.group())
print("? 0 or 1 time")
X=re.compile(r'Bat(wo)?man')
z=X.search("Advanture of Batman")
print(z.group())
z=X.search("Advanture of Batwoman")
print(z.group())
print(" * is zero or more ")
X=re.compile(r'Bat(Wo)*man')
# y=X.search("hye Wowoman")
# print(y.group())
# t=X.search("hye man")
# print(t.group())
print("denote start with^ and $  denote with endwith")
txt="the rain is. spain"
x=re.search("^the.*spain$",txt)
print(x.group())
print("wide space")
x=re.search("\s","the rain in spain")
print(x.start())
print("split function")
