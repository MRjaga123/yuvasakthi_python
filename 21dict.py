# A dictionary is a collection that is ordered* (as of Python 3.7), changeable, and does not allow duplicates. Dictionaries are written with curly brackets and have keys and values.

# 1. Creating and Accessing a Dictionary
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(dict1["brand"])  # Output: Ford
print(len(dict1))  # Output: 3

# 2. Dictionary with Multiple Types of Values
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(dict1))  # Output: <class 'dict'>

# 3. Accessing and Modifying Dictionary Data
x = dict1.get("model")
print(x)
x = dict1.keys()
print(x)
dict1["color"] = "white"
print(dict1)

# 4. Dictionary Methods
print(dict1.values())
print(dict1.items())
if "model" in dict1:
  print("Yes, 'model' is one of the keys")
dict1["year"] = 2018
print(dict1)

# 5. Updating, Removing, and Copying
dict1.update({"year": 2020})
dict1["color"] = "red"
dict1 = dict1.copy()
mydict = dict(dict1)
dict1.pop("model")
dict1.popitem()
del dict1["year"]
dict1.clear()
print(dict1)

# 6. Looping Through Dictionary
for x in dict1:
  print(x)
for x in dict1:
  print(dict1[x])
for x in dict1.values():
  print(x)
for x in dict1.keys():
  print(x)
for x, y in dict1.items():
  print(x, y)

##### Exercise
# Exercise 1: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict1={}
# dict1={keys[0]:values[0]}
for i in range(len(keys)):
  dict1.update({keys[i]:values[i]})
print(dict1)

# Exercise 2: Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

# Exercise 3: Access the value of key ‘history’ from the below dict
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict["class"]["student"]["marks"]["history"])

# Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
dict1={"details":[{"name":i,"default":defaults}for i in employees]}
print(dict1)

# Exercise 5: Create a new dictionary by extracting the following keys from a below dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
dict1={}
keys = ["name", "salary"]
for i in keys:
  if i in sampleDict:
    dict1.update({i:sampleDict[i]})
print(dict1)

# Exercise 6: Delete set of keys from a dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keysToRemove = ["name", "salary"]
for i in keysToRemove:
  if i in sampleDict:
    sampleDict.pop(i)
print(sampleDict)

# Exercise 7: Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sampleDict.values():
  print("true")
else:
  print("false")
    
# Exercise 8: Rename key city to location in the following dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sampleDict["location"]=sampleDict.pop("city")
print(sampleDict)

# Exercise 9: Get the key of a minimum value from the following dictionary
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
min_value=min(sampleDict.values())
min_key=min(sampleDict)
print(min_value)
print(min_key)

# Exercise 10: Change Brad’s salary to 8500 from a given Python dictionary
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict["emp3"]["salary"]=8500
print(sampleDict)

