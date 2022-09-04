# About class flow:


# 1. class define
#     a. arguments define 
#     b. define methods/function 
        # 1step define 
        #     a kya argument pass kar reaha hai 
        #         1 kitne argument pass 
        #             a. single, multipal, multipal arg as single argumen recive using * **
        #     b. function body logic 
        # 2step call fucntion 
        #     a. value pass karna 
        #     b. responce recive 
    # c. class object arguments
    #     a. __init__() ke thourgh 


# 2. class ka object 



# Python Classes and Objects

# class name me first character capital hoga

# ye class ko define kiya gaya hai
class MyFirstClass:
    print('\nHello my first class')

    def myFirstMethod():
        print('\nHello my first method.')
    
    def myFirstMethod1(a, b):
        return a*b
        # print('\nHello my first method.')

# class ka object bana rahe hai
# obj = new ClassName();

# myFirstObject objet ke thorught hum class ko access kar sakte hain.
# Matlab ki hum class ke variables aur mehtods ko call kar sakte hai.
myFirstObject = MyFirstClass
myFirstObject.myFirstMethod()

result = myFirstObject.myFirstMethod1(100, 10)
print('\nResult: ', result)
# myFirstObject.myFirstMethod()


# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# Create a Class
# To create a class, use the keyword class:


# Create Object
# Now we can use the class named MyClass to create objects:



# The __init__() Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:


# Object Methods


# The self Parameter


# Modify Object Properties


# Delete Object Properties


# Delete Objects


# The pass Statement



# Questions:
# About Object and class
# What is Python Inheritance
# Why use Python Inheritance
# How to use Python Inheritance
# What is oop's concept
# Why use oop's concept
# oop's concepts name