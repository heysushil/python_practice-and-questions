# Dictonary:

# key alwasy be in string
# key: value

smallDict = {'name': 'Daksh', 'course': 'Python'}

# Print only course:
# smallDict['course']
print('\nCoure name: ', smallDict['course'])

# doble layer dictonary:
midDict = {
    'personalInfo': {
        'name': 'Dakhs',
        'age': {
            'origanl': 28,
            'dublicate': {
                'dub1': 20,
                'dub2': 18,
                'dub3': 15,
            },
        },
    },
    'proInfo': {
        'school': 'ABC'
    }
}

# print('\nAge: ', midDict['personalInfo']['age']['origanl'])
print('\nAge: ', midDict['personalInfo']['age']['dublicate']['dub3'])

# cahnge dub3 age form 15 to 16
midDict['personalInfo']['age']['dublicate']['dub3'] = 16
print('\nAge: ', midDict['personalInfo']['age']['dublicate']['dub3'])

# midDict.


# Home work:

# check all dictonroy realted mehtos 
# learn about set

# condition: if else