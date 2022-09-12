# File Handling
# File: Create | Read | Update/Modify | Delete
# Inside File :  Modes
    # if file aleray exists: read (r)
    # if file not exists: append (a)
    # if write a file: write (w)
    #     if file not exits use w because w creates new file 
    #     else use x to open file in write mode because it will reamin previous data as on 
    # if write a file but not exists: create (x)

# use open() method to open file in read or write mode

# open file
# bioData = open('daksh_a.txt', 'a')
# print('\nCheck newly create file output: ', bioData)

# Create new file and enter few data
# bioData = 'Hello Daksh how are you?'
# bioData = input('\nEntery your bio data? \n')
# bioData = {
#     'Name': 'Daksh',
#     'Course': 'Python',
# }
bioData = '''Name: Daksh
Course: Python'''

# Check with w to override exising data
# openFile = open('daksh.txt', 'w')

# CHeck with x to append new data on fiel
openFile = open('daksh_2.txt','a')

# openFile.write('Hello Daksh how are you?')
openFile.write(bioData)
# close this file
openFile.close()

# open fiel again in read mode
readBioData = open('daksh.txt','r')
# readBioData.writ
# readBioData.write(bioData)
getData = readBioData.read()
print('\n', getData, '\n')
readBioData.close()