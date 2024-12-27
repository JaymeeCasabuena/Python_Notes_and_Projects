# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

"""
NOTES

Can only concantenate strings


"""

name = 'John'
age = 26
location = "Sydney"

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position using format method

"""
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}
The format() method returns the formatted string.

"""

# print("My name is {name} and I am {age}".format(name = name, age = age))


#named indexes:
# txt1 = "My name is {name}, I'm {age}".format(name = name, age = age)
#numbered indexes:
# txt2 = "My name is {0}, I'm {1}".format(name, age)
#empty placeholders:
# txt3 = "My name is {}, I'm {}".format(name, age)

# print(txt1)
# print(txt2)
# print(txt3)

# F-Strings (3.6+)

"""
F-string allows you to format selected parts of a string.
To specify a string as an f-string, simply put an f in front of the string literal, like this:
"""

# print(f'My name is {name} and I am {age} from {location}.')

# String Methods

s = 'hello world'

# Capitalize string
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

print(s.capitalize())


# Make all uppercase
print(s.upper())


# Make all lower
print(s.lower())

# Swap case
# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

print(s.swapcase())

# Get length

print(len(s))

# Replace
"""
The replace() method replaces a specified phrase with another specified phrase.

Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.

Parameters
string.replace(oldvalue, newvalue, count)
oldvalue - Required. The string to search for
newvalue - Required. The string to replace the old value with
count - Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
"""

print(s.replace('world', 'everyone'))

# Count
# The count() method returns the number of times a specified value appears in the string.

sub = 'h'
print(s.count(sub))


# Starts with
# The startswith() method returns True if the string starts with the specified value, otherwise False.

print(s.startswith('hello'))

# Ends with
# The endswith() method returns True if the string ends with the specified value, otherwise False.

print(s.endswith('d'))

# Split into a list
"""
The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.


parameters 

separator - Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit - Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
"""

t = "brisbane, sydney, melbourne"
print(t.split())
print(t.split(', '))
print(t.split(', ', 2))
print(t.split(', ', 0))



# Find position
"""
The find() method finds the first occurrence of the specified value.
The find() method returns -1 if the value is not found.
The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

Parameter
value - Required. The value to search for
start - Optional. Where to start the search. Default is 0
end - Optional. Where to end the search. Default is to the end of the string

end parameter is exclusive 
example

print(s.find('r', 5, len(s)))  # Searches from index 5 up to (but not including) 9

so len(s) - 1 won't work

"""

z = 'example234'

print(z.find('e'))
print(z.find('e', 5, len(s)))


# Is all alphanumeric
"""
The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
Example of characters that are not alphanumeric: (space)!#%&? etc.
"""
print(z.isalnum())

# Is all alphabetic
"""
The isalpha() method returns True if all the characters are alphabet letters (a-z).\
Example of characters that are not alphabet letters: (space)!#%&? etc
"""

print(z.isalpha())

# Is all numeric
"""
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
Exponents, like ² and ¾ are also considered to be numeric values.
"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
"""

print(s.isnumeric())
