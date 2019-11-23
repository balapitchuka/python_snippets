import os

# Note : Paths use Backslash on Windows and Forward Slash on OS X and Linux

# 1. use os.path.join(subpath1, subpath2, subpath3, ...) for joining files and folder names
print(os.path.join('usr', 'documents', 'log.txt'))

filenames = ['album.png', 'employee.txt', 'builder.bat']
for filename in filenames:
    print(os.path.join('C:\\Users\\bala', filename))

#2. print current working directory.
print(os.getcwd())

#3. change current working directory
current_dir = os.getcwd()
os.chdir('..')
print(os.getcwd())
os.chdir(current_dir)
print(os.getcwd())

#4. create new folders
os.makedirs('C:\\project\\examples\\test\\hello')
os.removedirs('C:\\project\\examples\\test\\hello')

#5.  easy way to convert a relative path into an absolute one
print(os.path.abspath('./basics.py'))

#6. check argument is absolute or relative path
print(os.path.isabs('./basics.py'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

#7.  return a string of a relative path from the start path to path(default start to current directory)
print(os.path.relpath('.\\basics.py', 'D:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

#8.  return a string of everything that comes before the last slash in the path argument
print(os.path.dirname(os.getcwd()))

#9. return a string of everything that comes before the last slash in the path argument
print(os.path.basename(os.getcwd()))

#10. print basename and directory name together
print(os.path.split(os.getcwd()))

#11.  print  a list of strings of each folder in the path
path = r'C:\\Windows\\System32\\calc.exe'
print(path.split(os.path.sep))


#12.  get the size in bytes of the file in the path argument
print(os.path.getsize('./basics.py'))

#13.  get list of filename strings for each file in the path argument
print(os.listdir())

#14. print the size of all files in path
total_size = 0
for file in os.listdir('C:\\Windows'):
    total_size +=  os.path.getsize(os.path.join('C:\\Windows', file))
print("-- Total size is :", total_size)