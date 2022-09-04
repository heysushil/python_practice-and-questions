buns = ['0. parmesan bread' , '1. oregano parmesan bread' , '2. wheat bread' , '3. premium bread']
print('\n', buns)
bunn = int(input('\nwhat kind of bread would you like: ')) 
vegetables = ['0. lettuce' , '1. tomato' , '2. onion' , '3. cucumber' , '4. corn']
print('\n', vegetables)
veggie1 = input('\nchoose your vegetable 1: ')
veggie2 = input('\nchoose your vegetable 2: ')
pattyoption = ['0. aloo tikki', '1. kebab patty', '2. chicken patty']
print('\n',pattyoption)
patty = int(input('\nchoose your patty: '))
saucy = ['0. mayonnaise', '1. jalapeno dip', '2. Cheese']
print('\n', saucy)
sauce = int(input('\nchoose sauce: '))
def burger(bun, veg1, veg2,patt,sauces):
    if bun == 0:
        print('\nbread chosen: ', buns[0])
    elif bun == 1:
        print('\nbread chosen: ', buns[1])
    elif bun == 2:
        print('\nbread chosen: ', buns[2])
    elif bun == 3:
        print('\nbread chosen: ', buns[3])
    else:
        print('\nerror: no such bread')
    if veg1 == '0':
        print('\nveggie1 chosen: ',vegetables[0])
    elif veg1 == '1':
        print('\nveggie1 chosen: ',vegetables[1])
    elif veg1 == '2':
        print('\nveggie1 chosen: ',vegetables[2])
    elif veg1 == '3':
        print('\nveggie1 chosen: ',vegetables[3])
    elif veg1 == '4':
        print('\nveggie1 chosen: ',vegetables[4])
    elif veg1 == '':
        print('\nno veggie selected')
    else:
        print('\ninvalid veggie chosen')
        exit()
    if veg2 == '0':
        print('\nveggie2 chosen: ',vegetables[0])
    elif veg2 == '1':
        print('\nveggie2 chosen: ',vegetables[1])
    elif veg2 =='2':
        print('\nveggie2 chosen: ',vegetables[2])
    elif veg2 == '3':
        print('\nveggie2 chosen: ',vegetables[3])
    elif veg2 == '4':
        print('\nveggie2 chosen: ',vegetables[4])
    elif veg2 == '':
        print('no veggie selected')
    else:
        print('invalid veggie chosen')
        exit()
    if patt == 0:
        print('\npatty chosen:', pattyoption[0])
    elif patt == 1:
        print('\npatty chosen:', pattyoption[1])
    elif patt == 2:
        print('\npatty chosen:', pattyoption[2])
    else:
        print('\ninvalid patty chosen')
        exit()
    if sauces == 0:
        print('\nsauce chosen: ', saucy[0])
    elif sauces == 1:
        print('\nsauce chosen: ', saucy[1])
    elif sauces == 2:
        print('\nsauce chosen: ', saucy[2])
    


print('''
===============================================================================================================
                            THANK YOU FOR WAITING HERE'S WHAT YOU ARE ORDERING
===============================================================================================================
''')
burger(bunn,veggie1,veggie2,patty,sauce)

