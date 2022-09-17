import os


class FileManagement():
    # method to check if file exits or not
    # def check_file_existence(self):
    #     try:
    #         if os.path.exists(fileName) == True:
    #             return True
    #         else:
    #             return False
    #     except NotADirectoryError:
    #         print('\nIt is not direcotry try to enter directory name.')
        # finally:                                            #prints it everytime function is called, we don't need that!
        #     print('\nFile check successfully.\n')
            
    def globname(self):
        global fileName
        fileName = input('\nEnter file name: ')
    def globInput(self):
        global userInput
        userInput = input('Enter option number: ')
    # method to create a fileName
    def create_file(self):        
        # check file exists or not
        self.globname()
        try:
            if os.path.exists(fileName) == True:
                print('\n',fileName, 'already exists, try with another name.')
                self.create_file()
            elif os.path.exists(fileName) == False and '.txt' in fileName:
                open(fileName, 'x')
                print('\nfile created successfully')
                self.wdyWanttoDo()
            elif fileName == '0':
                print('\noperation cancelled..')
                self.wdyWanttoDo()
            else:
                print('\nonly files with .txt extension are currently allowed')
                self.create_file()     
        except FileExistsError:
            print('\nFile already exists try with new name.')

    def delete_file(self):
        self.globname()
        try:
            if os.path.exists(fileName) == True and '.txt' in fileName:
                    os.remove(fileName)
                    print('\n', fileName,'is successfully deleted.')
                    self.wdyWanttoDo()
            elif '.txt' not in fileName:
                print('\nonly .txt files are currently allowed')
                self.delete_file()
            elif fileName == '0':
                print('\noperation cancelled')
                self.wdyWanttoDo()
            else:
                print('\n', fileName, 'does not exist.')
                self.delete_file()
        except:
            print('error came up in delete file')


    def wdyWanttoDo(self):
        print('''
        --------------------------------------
                FILE MANAGEMENT SYSTEM
        --------------------------------------
        Do you want to:
        1. create a new file
        2. delete an existing file
        3. edit a file
        4. read a file
        5. exit
         *type 0 mid-operation to cancel                 v2.1
        ''')
        self.globInput()
        if userInput == '1':
            print('\nyou have chosen to create a new file..')
            self.create_file()
        elif userInput == '2':
            print('\nyou have chosen to delete an existing file..')
            self.delete_file()
        elif userInput == '3':
            print('\nyou have chosen to edit an existing file..')
            DataLibrary.dataInfo(self)
        elif userInput == '4':
            print('\nyou have chosen to read an existing file..')
            DataLibrary.dataInfo(self)
        elif userInput == '5':
            print('\n program quit successfully')
            DataLibrary.dataInfo(self)
        else:
            print('\ninvalid input')
            self.wdyWanttoDo()


# Creating class to add data on file
class DataLibrary(FileManagement):

    def dataInfo(self):
        self.globname()
        try:
            if userInput == '3' and os.path.exists(fileName) == True:
                a =  open(fileName, 'a')
                p = '''
                -------------------------------------
                            EDITING {}
                -------------------------------------
                '''.format(fileName)
                print(p)
                editing = input('\nstart writing here:')
                a.write(editing)
                a.close()
                self.wdyWanttoDo()
            elif fileName == '0':
                print('\noperation cancelled..')
                self.wdyWanttoDo()
            elif userInput == '4':
                r = open(fileName, 'r')
                f = '''
                -------------------------------------
                        READING FROM {}
                -------------------------------------
                '''.format(fileName)
                print(f,r.read())
                r.close()
                self.wdyWanttoDo()
            elif userInput == '5':
                exit()
        except FileNotFoundError:
            print('no such file was found, try again')
            self.wdyWanttoDo()

            
fileOBJ = FileManagement()
fileOBJ.wdyWanttoDo()