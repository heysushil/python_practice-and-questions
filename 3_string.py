# String:

# single line stirng
# from array import array
# from curses import has_ic
# from unicodedata import category


name = 'Python' 

# multiline string
name = '''
Python
Python
Python
'''

# Array: list / tuple / dict / set
    # Array types in C/C++/JAVA/PHP
        # index array => signle or multi dimention array
        # associative array => dict/ set
        
    # list / tree / 
    # name = n a m e 
    # dict = a -> z 
    #         aaaaa->26 
    #         ab a-> 26
    #         ac a->26

    #         a / g / 
    #         book category -> 
    #             school / collage / normal 
    #                 class / degree / normal 
    #                     author / ->

    # Matrix:
    # 1   1   1
    # 7   7   7
    # 6   7   6 (3*3)

    # index value

    # array values ko hum 2 tarike se store karte hain kyo ki hame 2 tarki se store karne ki jarurat padti hai
        # Example:
        #     class room: class me 1 se jada student ke name same ho sakte hain to teacher unhe roll numer dete hai 
        #     school admition: school form me fields jarui hote hain

        # array value ko index wisee store karte hain
        # array values ko key => value ke pair me store kerte hain


# String: check index values
# string index 0 se start hota hai
# index range hamesa -1 tak hota hai.
    # example: name[0:3] yaha par ye 0 se 2 tak value dega but 3rd pos. ki value nahi dega becaue index range 0:3-1 tak chalega
name = 'hello string'
print('Length of Name: ', len(name))
# check 0 index of stirng
print('\n1st index value of name: ', name[0], '\n')
# string range
print('\nName range form 0 to 3: ', name[0:3])
# string range
print('\nName range form  to 3: ', name[:3])

print('\nName range form 5 to : ', name[6:])



# Modify stirng:
name = 'hello string modify'
print('Capitalize: ', name.capitalize())
print('upper: ', name.upper()) 

new_name = 'how are you?'
print(name,new_name) 


# Home work
    # stirng array related indexing / slicing ke example run karne hai 
    # string related sabhi method ke print case banae hain aur comment me define karna hai

    # ASCII ke bare me padhna hai
    # Operatores
    # List | tuple