import os
import sys
print(os.getcwd())
os.chdir("D:\python project")# change directory
print(os.getcwd())#cwd-current working directory
print(os.listdir(os.getcwd()))
print(os.path.abspath("list.py"))# it use for new create shows  file to create if file exist it show path of it.
# abspath-absolute path
print(os.path.isabs(os.getcwd()))
print(os.path.isabs("dict.py"))

direc=os.getcwd()
print(os.path.isabs(direc))
file=sys.argv[0]#argv- command line argument sys is module is check all over system it uses in file handling
print(file)
print(os.path.relpath("text.txt","d://"))
print(os.path.relpath("d://text.txt","filename"))
print(os.curdir)#current directory or current path
