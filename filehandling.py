import os
pa=os.getcwd()+"\ test.txt"
file=open(pa,'w')#w- this file wrie mode
file.write("hi")#in write we can write only one string for multiple line use write line
file.close()
#val='''this work as file handling working  in python'''
#file.write(val)
#file.close()
#file.writelines(["\tBye\n","hello"])
#file.close()
file=open(pa,'a')
file.write("\nNext file")
file.close()
file=open(pa,'r')
print(file.read())
for line in file.readlines():
    print(line,end=" ")
file.close()
