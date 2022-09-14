# open fiel again in read mode
readBioData = open('daksh.txt','r')
# readBioData.writ
# readBioData.write(bioData)
# getData = readBioData.read()
# getData = readBioData.readline(20)
getData = readBioData.readlines()
print('\n', type(getData), '\n')

# count length of list
print('\nTotal lines of getdata text file: ', len(getData), '\n')

# Get individual lines from getdata text file using for loop
i=1
for line in getData:
    print('Topic ',i,': ',line)
    i+=1
readBioData.close()