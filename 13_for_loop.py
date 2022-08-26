# for keyword

string_valule = 'Hi Dakhs how are you?'

# i intilize with 0 for showing index number on print in side for loop
i = 0
for val in string_valule:
    # 0 : H
    # 1 : i
    print(i, val)
    i += 1

biodata = {
    'name1': 'Dakhs 1',
    'name2': 'Dakhs 2',
    'name3': 'Dakhs 3',
    'name4': 'Dakhs 4',
    'name5': 'Dakhs 5',
    'name6': 'Dakhs 6',
    'name7': 'Dakhs 7',
    'name8': 'Dakhs 8',
}

for key in biodata:
# for key in biodata.values(): items()
    print('Name: ', biodata[key])
    # print('Name: ', key)
    
# Name  Age ClassName   School
for key in biodata:
    print(key, biodata[key])

for key, value in biodata.items():
    print(key, value)
