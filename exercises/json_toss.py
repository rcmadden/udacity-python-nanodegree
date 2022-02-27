# Write your code here :-)
import json

with open('data/cad.json', 'r') as file:
    print(type(file))
    jsonData = json.load(file)
    # if type is dict and count of keys < 50
    print((jsonData.keys()))
    print((jsonData['fields']))
    print(len(jsonData['fields']))
    print(len(jsonData['data']))
    print(type(jsonData['data']))
    print((jsonData['data'][0:3]))

