# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

# check = lambda a: pass
# check = lambda : 'Hello'
# print('\n', check())

def hello(a, b):
    # a,b = 10, 20
    check = lambda a,b: a * b
    print('\nMultiply: ', check(a,b))

hello(10,20)
