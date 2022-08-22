# List

# list use []
# tuple use ()

newvar = [1,2,3,4,5,6,7,8]

newvar[0] = 111
print('\nnewvar: ', newvar);exit()


newvar = (1,2,3,4,5,6,7,8) 

print('''
helajhdla
sjdfkak
kjasdkfah
jsakjfdsk
''') 

# List
mylist = [1,2,3,4,5,6,7,8]

mylist.append([1,2,3,4])

mylist = [
    [1,2,3,4,[1,2,3,4,5]],
    (2,3,4,5,6,[1,2,3,4,5],8),
    {'name':'Daksh','data':[1,2,3,4,5]},
]

print('\nmylist: \n',mylist ,'\n')
print('\nDetail: ', mylist[2])

# Casting: type casting: data type change

print('\nType of mylist: ', type(mylist))

# casting of list to tuple
listToTuple = tuple(mylist)
print('\nType of listtotuple: ', type(listToTuple))

# list to tuple then tuple to list
tupletolist = list(tuple(mylist))
print('\ntupletolist: ', type(tupletolist))




# Home work:

# Chek all methods of list and tuple
    # list methods 11
    # tuple methods 2

# Dict / set

