import os
import sys
import datetime
print(os.path.dirname("d:\python project\import.py"))
print(os.path.basename("import6.py"))# it shows dumy file
f=os.path.exists("dict.py")
print(f)
file=sys.argv[0]
print(file)
print(os.path.isdir("d:\python project\import1.py"))#directory
print(os.path.isfile("d:\python project\import.py"))#file

print(os.path.getsize("D:\python project\pr10.py"))
print(dir(os))# gives name of dir
print(help("os"))
print(help("random "))
#os.mkdir("d:\\python project\\newfile")
#os.removedir() when inside the subfolder are not in it
#os.removedirs() it remove directory subdirectory also
#os.remove("d:\\python project\\command.py")
#os.rename("d:\\python project\\pr11.py","d:\\python project\\pr9.py")
print(os.stat("d:\\python project\\pr8.py").st_size)
print(os.stat("d:\\python project\\pr8.py").st_mtime)
date=os.stat("d:\\python project\\pr8.py").st_mtime
print(datetime.datetime.fromtimestamp(date))
