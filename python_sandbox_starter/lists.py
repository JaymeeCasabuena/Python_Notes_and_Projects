# A List is a collection which is ordered and changeable. Allows duplicate members.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# From Python's perspective, lists are defined as objects with the data type 'list':


# Create list
numbers = [1, 2, 3, 4, 5]

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get the last value
print(fruits[-1])

# Get range of indexes
"""
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.

Note: The search will start at index 2 (included) and end at index 5 (not included).
"""
print(fruits) 
fruits[1:2] = ["Kiwi", 'Mango']
print(fruits) 



# Get length
print(len(fruits))

# Append to list
# The append() method appends an element to the end of the list.

fruits.append('Mangos')


# Remove from list
"""
The remove() method removes the specified item.
If there are more than one item with the specified value, the remove() method removes the first occurrence:
"""
fruits.remove('Grapes')

# Insert into position
"""
The insert() method inserts the specified value at the specified position.

pos - Required. A number specifying in which position to insert the value
elmnt - Required. An element of any type (string, number, object etc.)
"""
fruits.insert(4, 'Strawberries')


# Change value
fruits[0] = 'Blueberries'

print(fruits)


# Remove with pop
"""
The pop() method removes the specified index.
If you do not specify the index, the pop() method removes the last item.
"""
fruits.pop(2) # will remove pears
# fruits.pop() # will remove strawberries

print(fruits)


# Remove with del
"""
The del keyword also removes the specified index:
The del keyword can also delete the list completely.

"""

del fruits[-1] # will remove strawberries


# Clear the list
# The clear() method empties the list. The list still remains, but it has no content.

# fruits.clear()

# Reverse list
# The reverse() method reverses the sorting order of the elements.

fruits.reverse()

# Sort list
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

fruits.sort(reverse = True)

# Reverse sort
# To sort descending, use the keyword argument reverse = True:

fruits.sort(reverse=True)


