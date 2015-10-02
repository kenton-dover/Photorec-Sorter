#!/usr/bin/python3
'''this program was originally designed to sort photorec recovered file however,
it will now sort anything that you throw at it.
Note this program will create a duplicate of all the files make sure you have
Enough space to do this. This part is on you not the program.
This program is filed under the IDC (I don't care) License.'''
import os
import shutil


# This is the recursive function that goes through the directories
def progressor(path):
    files_in_source_dir = os.listdir(path)
    for file_in_source_dir in files_in_source_dir:
        new_path = os.path.join(path, file_in_source_dir)
        if os.path.isdir(new_path):
            progressor(new_path)
        else:
            evaluate(new_path)


def evaluate(path):
    # if the file_extension does not exsit it creals a null value
    filename, file_extension = os.path.splitext(path)
    # handles the null value
    if file_extension == '':
        file_extension = "extensionNotFound"
    elif file_extension[0] == '.':
        file_extension = file_extension.lstrip('.')
    if os.path.isdir(os.path.join(dest_file, file_extension)):
        print("Found the dir and copying the file: ", path)
        shutil.copy(path, os.path.join(dest_file, file_extension))
        # handles if there is now directory to sort into
    else:
        print("Could not find the dir. Creating one.")
        os.mkdir(os.path.join(dest_file, file_extension))
        print("Copying the file: ", path)
        shutil.copy(path, os.path.join(dest_file, file_extension))


# main method
def main():
    progressor(source_file)

# main function I'm used to this type of programming
if __name__ == "__main__":
    source_file = input("Enter the source file full path ending with /: ")
    dest_file = input("Enter the destination file fill path ending with /: ")
    main()
