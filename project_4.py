# Create class to create file or delete file
import os


class FileManagement():
    # crete construeter to reacie file name via user
    def __init__(self, fileName):
        self.fileName = fileName

    # method to check file is exits or not
    def check_file_existence(self):
        try:
            if os.path.exists(self.fileName) == True:
                return True
            else:
                return False
        except NotADirectoryError:
            print('\nIt is not direcotry try to enter directory name.')
        finally:
            print('\nFile check successfully.\n')
            

    # method to create a fileName
    def create_file(self):
        # check file is exist or not
        try:
            if self.check_file_existence == True:
                print('\n', self.fileName, 'is already exits, try with someother name.')
            else:
                open(self.fileName, 'x')
        except FileExistsError:
            print('\nFile Exists try with new name.')
        finally:
            print('\nFile work is completed.')

    def delete_file(self):
        if os.path.exists(self.fileName) == True:
                os.remove(self.fileName)
                print('\n', self.fileName,' is successfully deleted.')
        else:
            print('\n', self.fileName, 'is does not exits.')
        

# fileName = input('\nEnter file name: ')
# fileOBJ = FileManagement(fileName)
# fileOBJ.create_file()
# fileOBJ.delete_file()

# Create class to add info on file
class DataLibrary(FileManagement):
    pass


# Project:
# 1. Show to option to user 
#     1. Creat a file 
#         - call parent class metod to create a file using try except 
#     2. delete a file 
#         - call paret class method to delete file using try except 
#     3. Insert data 
#         - first get the file name by user in which he wants to insert data 
#         - then get data via user and insert it into provided file 
#     4. Exit 



# Error handling
# try:
#   try body
# except:
#   show customize error to user


# Future scoope:
# 1. validate user to create only .txt file.