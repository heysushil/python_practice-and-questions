import json

biodata = '{"name":"Daksh"}'
print('\nString data: ', biodata[:5])

# convert from str to dict
newdata = json.loads(biodata)
print(newdata)
print('\nName: ',newdata['name'])
print('\nType of biodata: ', type(newdata),'\n')

# convert dict to str
convertdata = json.dumps(newdata)
print('\nType of biodata: ', type(convertdata),'\n')
