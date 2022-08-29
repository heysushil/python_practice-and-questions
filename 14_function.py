# Function:
    # function 1: withou argmetn without return
    # function 2: with argument without reutn
    # function 3: without argurmtn with return
    # function 4: with argument with return

# def keywor use to deifne function
# Ye function ko define kiya gaya hai
# function bracket ke anadr hum arguments pass karte hain.
def functionName(a):
    pass
    # return variable ya value

# ye function call hai
functionName(2)

a = 12

# define a static sum function
# function without argument and without return value
def static_sum():
    a = 10
    b = 20
    result = a + b
    print('\nStatic sum result: ', result)
    print('\n')

# call static_sum function
static_sum()

# function with arguemtn and without return value
def sum_with_arguments(num1, num2):
    result = num1 + num2
    print('\nSum with 2 arguments result: ', result)

# call function with arguemtn and without return value

# static values pass on function
# sum_with_arguments(20, 20)

# define staic variable and pass it on function
# a = 50
# b = 100
# sum_with_arguments(a, b)

# define dyanamic varibale and pass it on funciton
# a = int(input('\nEnter first number: '))
# b = int(input('\nEnter second number: '))
# sum_with_arguments(a, b)

# List values pass on function
mynumbers = [10,20,30,40]
# sum_with_arguments(mynumbers[2], mynumbers[1])
# sum_with_arguments('Hello', 'Daksh')
# sum_with_arguments('20', '10')


# Pass dictionary value on function
mydictonary = {
    'num1': 100,
    'num2': 400,
}
sum_with_arguments(mydictonary['num1'], mydictonary['num2'])


# print()


# funciton with arguemtn and with return
def sum_with_argument_and_return_value(num1, num2):
    result = num1 + num2
    return result

sum_with_argument_and_return_value(400, 400)
