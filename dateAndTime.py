import json
x ={"name": "John", "age": 30, "married": true,
     "divorced": false,"children": ["Ann", "Billy"], "pets": Null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
myStr= json.dump(x)
print(myStr["divorced"])