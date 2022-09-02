# Normal function with arguments

# studenntAttendence() yaha par 1 arguemtn pass kiya gaya hai jo ki stu roll number hai
def studenntAttendence(*stuRollNo):
    # single student ka rollnumber print karne ke liye
    # print('\n Roll No.', stuRollNo, 'is present.')

    # multipal sutdnets ka rollnumeb print karne ke liye for loop ka use karenge.
    for roll in stuRollNo:
        print('\n Roll No.', roll, 'is present. Type: ',type(stuRollNo))

# studnets valriable me humne list type value pass kiya because hame multipal numebrs cahiye the.
# students = [1,2,3,4,5,6]
studenntAttendence(1,2,3,4,5,6)

# Example of function with arguemtns and retun value

# Jio ka sime: aru ho sakta hai | return value
# jio ki compnay jiska sim hai: variable jo bhar se aa raha hai | function define
# jio ka reprensetative jo sime dega: call karenge | retrun
# dakhs jisko sim cahiye hai: function ho sakta hai | value

# function hota kya kya hai:
# define kiye: logic in side
# arugemtns pass kiya
# call kiya



# Arbitrary Arguments, *args
def studenntAttendence(*stuRollNo):
    # multipal sutdnets ka rollnumeb print karne ke liye for loop ka use karenge.
    for roll in stuRollNo:
        print('\n Roll No.', roll, 'is present. Type: ',type(stuRollNo))

studenntAttendence(1,2,3,4,5,6)


# Arbitrary Keyword Arguments, **kwargs
def studentBioData(**name):
    print('\n', type(name) ,' is present.')

studentBioData(name='Daksh',Class='12')
# bioData = {
#     'name':'Dakhs',
#     'class':12,
#     'age':20
# }
# studentBioData(bioData)

# Default Parameter Value
def meriMarji(name='', age='', myclass=''):
    print('\nHello,',name)

meriMarji()