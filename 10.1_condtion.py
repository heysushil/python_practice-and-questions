# use double condiiton:
name = 'Daksh'
name2 = 'Ram'
name3 = 'Shyam'

if name == 'Daksh':
    print('\nHi', name , '\n')
    # else name2 == 'Ram' and name3 == 'Shyam':
else:
    print('\nHello ' + name2 + ' and ' + name3 + '\n')

# and = and me sabhi condtion ture hogi tabhi hum condtionn me enter karenge
# or = koi bhi ek cond. sahi hue hum condtion me enter kar lenge
# not = ye condtion ko accetp nai karenge iske alawa koi bhi conditon ho to enter karn lenge

if name != 'Daksh':
    print('\nHi', name , '\n')
    # else name2 == 'Ram' and name3 == 'Shyam':
else:
    print('\nHello ' + name2 + ' and ' + name3 + '\n')


if name == 'Daksh' or name == 'Ram' or name == 'Shyam':
    print('\nHi', name , '\n')
    # else name2 == 'Ram' and name3 == 'Shyam':
else:
    print('\nHello ' + name2 + ' and ' + name3 + '\n')

if name == 'Daksh' and name2 == 'Ram' and name3 == 'Shyam':
    print('\nHi', name , ' all condtion are true.\n')
    # else name2 == 'Ram' and name3 == 'Shyam':
else:
    print('\nHello ' + name2 + ' and ' + name3 + '\n')


if not(name == 'Daksh1'):
    print('\nHi', name , '\n')
    # else name2 == 'Ram' and name3 == 'Shyam':
else:
    print('\nHello not elese part \n')

# identity opr: is / is not
print('\ncheck name is Daksh or not: ', name is 'Daksh', '\n')
print('\ncheck name is Daksh or not: ', name is not 'Daksh', '\n')

# memebershitp orp: in / not in
name = ['daksh','ram','shyam','radha']
print('\nIs Daksh in name: ', 'daksh' in name)


# Multi condtions

# store dict value using input
bio_data = {
    'name': input('\nEnter your name: '),
    'mobile': int(input('\nEnter your mobile: ')),
    'email': input('\nEnter your emial id: '),
}

my_data = '''\n
    Hi my name is {} and my other details are as followes,
    Mobile: {}
    Email ID: {} \n
    '''.format(bio_data['name'], bio_data['mobile'], bio_data['email'])
greeting = '''\n
----------------------------
        Hi, {}
----------------------------        
'''.format(bio_data['name'])

if bio_data['name'] == 'Daksh':
    # my_data = '''\n
    # Hi my name is {} and my other details are as followes,
    # Mobile: {}
    # Email ID: {} \n
    # '''.format(bio_data['name'], bio_data['mobile'], bio_data['email'])
    print(greeting)
    print(my_data)

elif bio_data['name'] == 'Ram':
    print(greeting)
    print(my_data)
elif bio_data['name'] == 'Shyam':
    print(greeting)
    print(my_data)
else:
    print(my_data)

if name == 'Ram':
    pass

name = 'Ram'


# Home work
# Program:
    # 1. user se input le kar chek karna hai ki wo jo value print kiya hai uska type kya hai wo kitne length ka hai.
        # Is ko multiline string me kuch ayse show karna hai
        # Your input is:
        # Value name: 
        # value type:
        # value length:

    # 2. use ka bio data dictonary me store kara kar usko check karna hai user ka input null to nahi hai then multiline string ka use kar kar output show karwana hai.
        # input galat hai to else me message show karna hai agian input ke liye.