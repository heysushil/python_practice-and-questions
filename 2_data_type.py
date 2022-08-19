import numbers


name = 'Python'

# condition exm.
# if ke bad name ek vaibalr hai
# == condition hai jo check kar raha hai ki name python ke barabar hai ya nahi
if name == 'Python':
    # ye print mehtod if condtion ka par hai 
    # yaha par `if print` ek string hai aur name ek varibale
    print('if print: ', name)
print('Outer if print:', name) # ye print mehtod if ka part nahi hai.

print('Name var type: ', type(name))


# Data Type:
    # Number: int, float, complex
    # Alphabet: string, bool, binary
    # Special Char
    # Audio
    # video



# Home work
# Github account: 
    # 1 repository create karna hai -> isme python code upload karna hai.
# Learn about git
# Diff b/w git and github
# stackover flow account 
# Special char ke name: () [] {} ,. : ; "" '' * # / \ | & $

# Kal ki class:
# numbers
# casting 
# string 
# boolean 

# operator 

# Data Types:

# Numbers:

# Note: varibale define karne ke 2 best tarike
    # 1: using underscore (_)
    # 2: using second words first char capital (intNum)
int_num = 10
float_num = 10.10
complex_num = 1j

# f sort form hai `format() method ka`
# f ke bar starting 3 and ending 3 coloum  use kiye gaie hain multi line string ke liye.
# multi line string me {} bracket ka use kiya hai vairable ki value access karne ke liye
# {} bracket ke andar hum method ya class bhi call kar sakte hain like as type() class 
result = f'''
int_num = {int_num} : Type -> {type(int_num)}
float_num = {float_num} : Type -> {type(float_num)}
complex_num = {complex_num} : Type -> {type(complex_num)}
'''

print(result)

# Number casting: 
# int => float
# float => int
# int => complex
# float => complex
# complex => int
# complex => float

# Text / Number casting:
# int => str '687368278'
# float => str
# str => int
# str => float


# print() method me humne 6 argument pass kiya hai
# 1st strign hai, 2nd variable 3rd string, 4th int() class use to convert flaot number into intiger, 5th sting, 6th call type() object to pass int() object into it to conver float num to int and check type of it. 
print('Float number conver into int: Flaot: ', float_num, ' => ', int(float_num), ' Type of convert value: ', type(int(float_num)))

# Boolean
check_bool_true_false = bool(int_num)
print('Check boolean of int_num: ', check_bool_true_false)

a = 10
check_bool_true_false = bool(a < 10)
print('check_bool_true_false: ', check_bool_true_false)


# Home work:
# Check casting and create some use cases:
    # int()
    # float()
    # complex()
    # str()

# Multiline stirng ka use karke apna bio data bana hai.
# Exampele:

# name, age, email = 'Devesh', 20, 'email'

# ---------------------------------------
#         Bio-Data
# ---------------------------------------
# Name: You_name
# Age:
# Mobile:
# Collage:
# Address:
# ----------------------------------------

# Operator
# List, tuple, dict, set: