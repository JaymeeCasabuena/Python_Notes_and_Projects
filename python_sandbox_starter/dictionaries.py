# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':


"""
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Duplicate values will overwrite existing values
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'age': 25
}

print(person) # age: 25


# Get value
print(person['first_name']) # Get the value of the "model" key

# There is also a method called get() that will give you the same result:

print(person.get('last_name')) 

# Add key/value
person['phone'] = '555-555-5555'

# The update() method will update the dictionary with the items from the given argument.

person.update({"location": "Sydney"})

# Get dict keys
# The keys() method will return a list of all the keys in the dictionary.

print(person.keys())

# Get dict values
# The values() method will return a list of all the values in the dictionary.


print(person.values())

# Get dict items
# The items() method will return each item in a dictionary, as tuples in a list.

print(person.items()) 

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword

if "age" in person:
    print("Yes")

# Copy dict - similar to spread operator in JavaScript
person2 = person.copy()
person2['Pronouns'] = 'He/Him'

# Another way to make a copy is to use the built-in function dict().

person3 = dict(person)
print(person3)

# Remove item
# The del keyword removes the item with the specified key name
# The del keyword can also delete the dictionary completely

del(person['age'])

# The pop() method removes the item with the specified key name:
# person2.pop('phone')

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

person2.popitem() # removed last item since version is not yet 3.7

print(person2)

# Clear empties the dictionary

person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])

# Loop Dictionaries

# Print all key names in the dictionary, one by one
for x in person2:
  print(x)

# Print all values in the dictionary, one by one

for x in person2:
  print(person2[x])

# or using values method

for x in person2.values():
  print(x)

# get all keys using the method

for x in person2.keys():
  print(x)

# Loop through both keys and values, by using the items() method

for x, y in person2.items():
  print(x, y)


# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

# loop using items method

for x, obj in myfamily.items(): # loop through both keys and values, print the key and then create an inner loop to get all nested values
  print(x)

  for y in obj:
    print(y + ':', obj[y])