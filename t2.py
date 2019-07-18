print("welcome on mini game ")
from random import choice as  ran
l=[1,2,3]
l[0]='snake'
l[1]='water'
l[2]='gun'
print("choose between from them \n 1=snake \n 2= water\n 3= gun")
system=ran(l)
user=input()
if user==system:
    print("game draw")
elif user==1 and system==2:
    print("you are won\n snake drink all water")
elif user==1 and system==3:
    print("you are loss gun shoots snake \n snake no more")
elif user==2 and system==1:
    print("you loss")
elif user==2 and system==3:
    print("you won")
elif user==3 and system==1:
    print("you won")
elif user==3 and system==2:
    print("you loss")
else:
    print("play according to game rule \n you choosen wrong")