# Sliing
# positive 0 1 2 3 4 
# negative -1 -2 -3
          # 4  3  2
string = 'hello hi how are you kai ho badhya ho .......'

# string concatenation
name = 'Daksh'
age = 10
course = 'Python'

# message = f'Hello Mr. ' + name + ', how are you?' + {age} + ' ' + course
# message = f'Hello Mr. ' + name + ', how are you?' + str(age) + ' ' + course
# print(message)


# string formate()
# message = 'Hello Mr. ' + name + ', how are you?' + {age} + ' ' + course + ''.format(age)

# formate() method string me valeus ko inded form ya fir key=value ke form me pass karta hai.
message = '''\n\nHello Mr. {n}, how are you? You age is {a} and you are learning {c}\n'''.format(a=age,c=course,n=name)
print(message)

# 


# Home work

# Line number 12 and 13 have this error. find our why?
    # Traceback (most recent call last):
    #   File "e:\xampp\htdocs\python_practice-and-questions\4_string_methods.py", line 12, in <module>
    #     message = f'Hello Mr. ' + name + ', how are you?' + {age} + ' ' + course
    # TypeError: can only concatenate str (not "set") to str 

    # Using format() method create same biodata but using key=value in formate.