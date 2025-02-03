
"""
By default, the .sort() method sorts the elements in ascending order in-place. 
The return value of the .sort() method is None.

In simple words, sort mutates the original list rather than creating and returning a new sorted list.

In contrast, built-in function sorted(), it returns a new sorted list without modifying the original
"""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort()
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort()
    return numbers



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

"""
The .sort() method also accepts some optional parameters. This is the .sort() function signature:

def sort(key=None, reverse=False) -> None:

The key parameter allow to customize the sorting order. 

The reverse parameter is a boolean value that determines whether the list should be sorted in descending order. By default, it is set to False.
"""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort(reverse=True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort(reverse=True)
    return numbers



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

#Sort Custom

"""
The key parameter doesn't accept a value, instead, 
it accepts a function that returns a value to be used for sorting.

"""

#example

def get_word_length(word: str) -> int:
    return len(word)

words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]

words.sort(key=get_word_length)

print(words) # ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']


"""
In the example above, we defined a function get_word_length that returns the length of a word. 
We then passed this function as the key parameter to the .sort() method. 
This means the words will be sorted based on their length, in ascending order, 
and not based on their lexicographical order.

"""

from typing import List

def get_word_length(word):
    return len(word)

def get_absolute_number(number):
    return abs(number)


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=get_word_length, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=get_absolute_number)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))


# sort lambda

"""
It is faster to use a lambda function to define a function in a single line and pass it directly to the .sort() method.

A lambda function can take any number of arguments, but can only have one expression.

lambda arg: expression

"""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=lambda word: len(word), reverse=True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=lambda n: abs(n))
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

# Sorted

"""
The sorted() function returns a new list with the elements sorted in the specified order. 
The original list remains unchanged.

The sorted() function takes the list as the first argument and returns 
a new list with the elements sorted in ascending order by default.

sorted(iterable, key=key, reverse=reverse)
"""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    words_sorted = sorted(words)
    return words_sorted


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers_sorted = sorted(numbers, key=lambda n: abs(n), reverse=True)
    return numbers_sorted


# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))

# SUMMARY 

"""
.sort() sorts the list in ascending order in-place and returns None.
It directly mutates the original list rather than making a new one.

sorted() returns a new sorted list without changing the original list.
Use it when you need the original list unchanged.

Optional Parameters (key & reverse):
.sort() accepts a key function to extract a sorting criterion and a reverse flag to sort in descending order.
Set reverse=True to sort in descending order.

Key Functions & Lambdas:
The key parameter takes a function (or lambda) that returns the value used for sorting.
Lambda functions provide a concise inline way to define such sorting criteria.

"""
