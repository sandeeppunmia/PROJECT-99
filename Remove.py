import os

path = 'C:/Users/Admin/pythonprojects/project-99/walk/'
for root,dirs,files in os.walk(path,topdown=True):
    print(root)
    print(dirs)
    print(files)
    print('----------------------------------')