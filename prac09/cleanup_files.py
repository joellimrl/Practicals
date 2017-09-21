"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os
from urllib import request


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics')
    # print a list of all files (test)
    print(os.listdir('.'))

    web = request.urlopen("https://www.google.com")
    print(web.read())
    """
    info = {}
    for each in os.listdir("."):
        if os.path.isdir(each):
            os.chdir(each)
            for filename in os.listdir('.'):
                with open(filename) as temp_file:
                    fileData = temp_file.readlines()
                    x = 0
                    for lines in fileData:
                        if lines[0:2] == ".i":
                            x = 1
                    if x == 0:
                        info[filename] = os.path.abspath(filename)
            os.chdir('..')
    print("This is the list of files missing the copyright information line: ")
    for each in info:
        print("{:35}: {}".format(each, info[each]))
    """
    # make a new directory
    # os.mkdir('temp')
    # extensions = {}
    # tempList = []
    # for filename in os.listdir('.'):
    #     ext = filename.split(".")[1]
    #     if ext not in tempList:
    #         tempList.append(ext)
    #         extensions[ext] = input("What category would you like to sort {} files into? ".format(ext))
    # print(extensions)
    # # loop through each file in the (original) directory
    # for filename in os.listdir('.'):
    #     # ignore directories, just process files
    #     if not os.path.isdir(filename):
    #         ext = filename.split(".")[1]
    #         if not os.path.isdir(extensions[ext]):
    #             os.mkdir(extensions[ext])
    #         shutil.move(filename, extensions[ext])

            #new_name = get_fixed_filename(filename)
            #print(new_name)

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()

        # os.chdir('..')  # .. means "up" one directory
        # for dir_name, subdir_list, file_list in os.walk('.'):
        #     print("In", dir_name)
        #     print("\tcontains subdirectories:", subdir_list)
        #     print("\tand files:", file_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    new_name = ""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    previousSpace = False
    new_name += filename[0].upper()
    for each in filename[1:]:
        if each.isupper():
            if previousSpace:
                new_name += each
                previousSpace = False
            else:
                new_name += "_" + each
        elif each.islower():
            if previousSpace:
                new_name += each.upper()
                previousSpace = False
            else:
                new_name += each
        elif each == "_":
            new_name += each
            previousSpace = True
        elif each == ".":
            new_name += ".txt"
            break
        else:
            new_name += each
    return new_name


main()