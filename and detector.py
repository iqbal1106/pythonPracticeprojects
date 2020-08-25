

#
# from os import listdir
# from os.path import isfile, join
# onlyfiles = [f for f in listdir("C:\Users\iqbal\PycharmProjects\") if isfile(join("C:\Users\iqbal\PycharmProjects\", f))]


from os import walk

# f = []
# for (dirpath, dirnames, filenames) in walk("C:\Users\iqbal\PycharmProjects\"):
#     f.extend(filenames)
#     break
#
# from os import walk
#
# f = []
# for (dirpath, dirnames, filenames) in walk(mypath):
#     f.extend(filenames)
#     break
#


import os

# # Getting the current work directory (cwd)
# thisdir = os.getcwd()
# count=0
# # r=root, d=directories, f = files
# for r, d, f in os.walk(thisdir):
#     for file in f:
#         if file.endswith(".py"):
#             print(os.path.join(r, file))
#             count=count+1
#             print(count)

# Getting the current work directory (cwd)
# thisdir = os.getcwd()    -----------didnot worked above code for files worked
# count=0
# # r=root, d=directories, f = files
# for r, d, f in os.walk(thisdir):
#     for directories in d:
#         if directories.endswith("PycharmProjects"):
#             print(os.path.join(r, f))
#             count=count+1
#             print(count)

# import os      **********worked
#
# arr = os.listdir('.')
# print(arr)
# count =0
# x = os.listdir('..')
# for i in x:
#
#     count=count+1
#     print(x,count)
# for i in x:
#     count=count+1
#     print(f" count of list directories are :{count(x)}")

# Method 2
#x= os.listdir('/')

# import glob
# count=1
# txtfiles = []
# for file in glob.glob("*.py"):
#     txtfiles.append(file)
#     count=count+1
# print (count,txtfiles)

# import os--- worked for current workig directory
#
# files_path = [os.path.abspath(x) for x in os.listdir()]
# print(files_path)

# #
# import pathlib
# pathlib.Path(__file__).parent.absolute()
# from pathlib import Path
# print("File      Path:", Path(__file__).absolute())
# print("Directory Path:", Path().absolute())

# import os
# dir_path = os.path(os.path.realpath(__file__))
#
# from pathlib import Path
#
# # Returns the path of the directory, where your script file is placed
# mypath = Path().absolute()
# print('Absolute path : {}'.format(mypath))
#
# # if you want to go to any other file inside the subdirectories of the directory path got from above method
# filePath = mypath / 'data' / 'fuel_econ.csv'
# print('File path : {}'.format(filePath))
#
# # To check if file present in that directory or Not
# isfileExist = filePath.exists()
# print('isfileExist : {}'.format(isfileExist))
#
# # To check if the path is a directory or a File
# isadirectory = filePath.is_dir()
# print('isadirectory : {}'.format(isadirectory))
#
# # To get the extension of the file
# fileExtension = mypath / 'data' / 'fuel_econ.csv'
# print('File extension : {}'.format(filePath.suffix))

# quote = "life, uh, finds a way"
# unique_vowels = {i for i in quote if i in 'aeiou'}
# print(unique_vowels)

squares = {i: i *i for i in range(10)}
print(squares)