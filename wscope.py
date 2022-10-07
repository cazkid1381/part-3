import json
class myJsonFile:
# some JSON:
    x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
    y = json.loads(x)

# the result is a Python dictionary:
myobj = myJsonFile()
read_age = myobj.y["age"]
print(read_age)
