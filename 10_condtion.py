# Condtion: keyword= if / else / elif (elseif)

# name is variable
# Daksh is value
# = assignment operator
# from curses.ascii import isalpha


name = 'Daksh'
name = input('\nEnter your name: ')

# Check value is equal or not
if name == 'Daks':
    # output: print()
    print('\nHello,', name)
else:
    print('\nName is not matching.')

# print('\nChck aplha: ', name.isalpha());exit()

# Check if name is stirng or not
if name.isalpha() == True:
    print('\nHi,', name ,'\n')
else:
    print('\nName must be only follow alphabets.\n')


# Add two number getting by user:
num_1 = input('\nEnter first number: ')
num_2 = input('\nEnter second number: ')

print('\nSum: ', num_1 + num_2)


# How to prevent user input only to int numebr
num_1 = input('\nEnter first number: ')
num_2 = input('\nEnter second number: ')

# print(num_1.isdigit())
if num_1.isdigit() == True:
    print('\nSum of num1 and num2: ', num_1 + num_2)
else:
    print('\nNon-interger number not allowed try again.')

# Home work:

# Check how many keyword availabale in Python/C/C++
# Linke number 28 to 32. perform sum 
# Line number 35 to 43.
    # Duble condtion lagan hai line number 40 par ki num 1 and num 2 dono hi jab inter ho tab if me aaye aur waha input print karana hai.
# Condtion bana hai odd aur even number chaeck karnke ke liye.
# 2n-1 / 2n %



# Note:
# Programming languages:
    # machine level lan. | binary
    # Low language       | nimonic mul=multiplication sum=additin sub
    # High Lev. lan      | 