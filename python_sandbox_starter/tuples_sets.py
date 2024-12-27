# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
# Otherwise Python will not recognize it as a tuple.

# From Python's perspective, tuples are defined as objects with the data type 'tuple':
print(type(fruits)) #<class 'tuple'>

fruits2 = ('Mango',)

# Get value
print(fruits[1])
# Range of indexes 
# Note: The search will start at index 12 (included) and end at index 3 (not included).
print(fruits[1:3])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
# del fruits2

# Get length
print(len(fruits))

"""
Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
"""

fruits += fruits2
# print(fruits)

# Unpacking Tuples
# The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

(a, *b, c) = fruits #Apples ['Oranges', 'Grapes'] Mango

# If the asterisk is added to another variable name other than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

print(a, b, c)

# Count - Returns the number of times a specified value occurs in a tuple

print(fruits.count("Oranges"))

# Index - Searches the tuple for a specified value and returns the position of where it was found

print(fruits.index("Mango"))


# A Set is a collection which is unordered and unindexed. No duplicate members.
# Note: Set items are unchangeable, but you can remove items and add new items.
# From Python's perspective, sets are defined as objects with the data type 'set'

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango', "Apples"} # Duplicate values will be ignored

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates

s = {1, True, "John", False, 0}

print(fruits_set)
print(s) # True and 0 are ignored


# Check length 

print(len(s)) 
print(type(s)) # <class 'set'>


# set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Add to set
fruits_set.add('Grape')


# Remove from set using remove method or discard
# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set - empty but still defined
# fruits_set.clear()

# Delete - delete the set completely
# del fruits_set

# print(fruits_set)

# Accessing sets

"""
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""
for x in thisset:
  print(x)


# Check if in set
print('apple' in thisset) #true

# Check if not in set

print("banana" not in thisset) #false


# Join Sets
"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

"""

set1 = {"a", "b", "c", "a"}
set2 = {1, 2, 3, 3}
tuple1 = ("s", "t", "u", "v")

# set3 = set1 | set2
# print(set3)

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

"""
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
The update() changes the original set, and does not return a new set.
Note: Both union() and update() will exclude any duplicate items.

"""

set1.update(set2) 
print(set1, "updated")

set2.update(tuple1) 
print(set2, "updated")

# The intersection() method will return a new set, that only contains the items that are present in both sets.

# set4 = {"apple", "banana", "cherry"}
# set5 = {"google", "microsoft", "apple"}

# set6 = set4.intersection(set5)
# print(set6) # apple - the duplicate

# You can use the & operator instead of the intersection() method, and you will get the same result.

# set4 = {"apple", "banana", "cherry"}
# set5 = {"google", "microsoft", "apple"}

# set6 = set4 & (set5)
# print(set6) # apple - the duplicate

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

# set4 = {"apple", "banana", "cherry"}
# set5 = {"google", "microsoft", "apple"}

# set4.intersection_update(set5)
# print(set4) # apple - the duplicate

# The values True and 1 are considered the same value. The same goes for False and 0.

set4 = {"apple", 1,  "banana", 0, "cherry"}
set5 = {False, "google", 1, "apple", 2, True}

set6 = set4 & (set5)
print(set6) # {False, 1, 'apple'}

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set7 = {"apple", "banana", "cherry"}
set8 = {"google", "microsoft", "apple"}

# or use - operator
set9 = set7.difference(set8) # {'banana', 'cherry'} not present in the set8

print(set9)

# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# opposite of intersection 
"""
If you imagine a Venn diagram:

intersection is the overlap (middle area).
symmetric_difference is everything outside the overlap (exclusive to each set).

"""

set10 = {"apple", "banana", "cherry"}
set11 = {"google", "microsoft", "apple"}

# or use ^ operator
set12 = set10 ^ set11

print(set12) # {'cherry', 'banana', 'google', 'microsoft'}

# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

set13 = set12.copy()
print(set13)