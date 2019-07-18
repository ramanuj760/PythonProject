import os
print(os.getcwd())
#os.mkdir("d:\\python project\\test1\\directory")
os.chdir("d:\\python project\\test1\\directory")
print(os.getcwd())
print(os.path.join(os.getcwd(),"word.txt"))
f1="d:\\python project\\test1\\directory"+"\ word.txt"
file=open(f1,'w+')
file.write("hello i am creating new file \n")
file.close()
file=open(f1,'a')
w='''When a new day begins, dare to smile gratefully
When there is darkness, dare to be the first to shine a light
When there is injustice, dare to be the first to condemn it
When something seems difficult, dare to do it anyway.
When life seems to beat you down, dare to fight back.
When there seems to be no hope, dare to find some.
When you’re feeling tired, dare to keep going.
6When times are tough, dare to be tougher.
When love hurts you, dare to love again.
When someone is hurting, dare to help them heal.'''
file.write(w)
file.close()
file=open(f1,'r')
print(file.read())
for line in file.readline():
    print(line,end= " ")
file.close()
