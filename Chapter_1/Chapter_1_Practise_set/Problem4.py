# Q4. Write a program to print the contents of a directory using os module.
# Search online for the function which does that.

import os
#Specify the path of the directory you want to list
directory_path='/'

#List the contents of the directories in the specified path
contents=os.listdir(directory_path)

#Print the contents of the directory
for item in contents:
    print(item)