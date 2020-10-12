import json

courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'

# Loads method parse json string and it returns dictionary

dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses['name'])

# get the first language

# list_language = dict_courses['languages']
# print(type(list_language))
# print(list_language[0])

print(dict_courses['languages'][0])


# Parse content present in Json file
with open('parse_org.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])

# price of course RPA

    print(type(data['courses']))
    for course in data['courses']:
        print(course)
        if course['title'] == "RPA":
            print(course['price'])


with open('parse_copy.json') as fi:
    data2 = json.load(fi)
    print(data == data2)
