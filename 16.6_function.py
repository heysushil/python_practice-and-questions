# Function me other function ko call karna

def learn_scooty(age):
    if age < 12:
        print('can\'t learn scooty yet')
    elif age > 12 and age < 26:
        print('500 rupiya lagegi')
    elif age > 26 and age < 50:
        print('1000 rupiya lagega')
    elif age >50 and age <100:
        print('2500 rupiya lagega')

def checkAgeIsInt(age):
    if age.isdigit():
        learn_scooty(int(age))
    elif age.isalpha():
        print('\nAlph values not allowed.')
    elif age.isalnum():
        print('\nAlph numeric values not allowed.')
    else:
        print('\nSpecial char not allowed.')

# user_age = int(input('what is your age: '))
age = input('what is your age: ')
# 'hello'.isdigit #isalpha #isalnum
# print(age.isdigit())
# learn_scooty(user_age)
checkAgeIsInt(age)



# About adv. of funcio
# 1step define 
#     a kya argument pass kar reaha hai 
#         1 kitne argument pass 
#             a. single, multipal, multipal arg as single argumen recive using * **
#     b. function body logic 
# 2step call fucntion 
#     a. value pass karna 
#     b. responce recive 




Question:

1. what is the max lenght of aruments in funciton define?