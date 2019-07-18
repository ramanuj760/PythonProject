import os
import sys
print(os.walk(os.getcwd()))#walk on complete  directory it read all path and its hold list of tuple
#for dirname,dirpath,filename in os.walk("d:\\movies"):
 #   print(dirname)
  #  print(dirpath)
   # print(filename)
print(os.environ.get("path"))
print(os.path.join(os.getcwd(),"text.txt"))