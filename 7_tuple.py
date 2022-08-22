# Tuple

from trace import CoverageResults


mytuple = (1,2,3,4,5,6,7)

# mytuple[0] = 111;
print('\nmytuple: ', mytuple);
# mytuple = (1,2,3,4,5,6,7,8)

print('\nmytuple: ', type(mytuple), '\n')

# convert tuple to list for update 0 index value 
convertTupleToList = list(mytuple)
convertTupleToList[0] = 111

# convert list to tuple
mytuple = tuple(convertTupleToList)

print('\nConvert list to tupel: Type: ', type(mytuple), '\n\n', mytuple, '\n')


# Home work:

# Create list: list ke index par dictonary data store kaarna hai jaise ki:
    # 0: personal data 
    # 1: prof data 
    # 2: about us 
    # 3: hobies

    # convert into tuple then print into multi line stirng

    # print using mulitline stirng
