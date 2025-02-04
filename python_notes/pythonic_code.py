# Unpacking


point1 = [0, 0]
point2 = [2, 4]

x1, y1 = point1 # x1 = 0, y1 = 0
x2, y2 = point2 # x2 = 2, y2 = 4

"""
This is called unpacking. We know point1 and point2 are lists of size 2, 
so we can unpack them into two variables each.
Unpacking also works with tuples and sets with the same syntax.

If we attempt unpacking with too many variables on the left-side, we will get a ValueError.
"""

x, y = [0, 0, 0] # ValueError: too many values to unpack (expected 2)

from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    a, b, c = triplet
    return a + b + c


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    w, h, d = box_dimensions
    return w * h * d
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))


# Loop Unpacking

"""
We can also use unpacking in loops to iterate over a list of lists. 
This is useful when we know the size of the inner lists and want to unpack them into variables.

"""
points = [[0, 0], [2, 4], [3, 6], [5, 10]]
for x, y in points:
    print(f"x: {x}, y: {y}")



from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    max_score, student = 0, ''
    for name, score in scores:
        if score > max_score:
            max_score, student = score, name
    return student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))


#Enumerate

"""
The enumerate() function returns a tuple of the index and the element at that index. 
We can unpack this tuple into two variables in the for loop.

"""

nums = [2, 7, 9, 2]

for i, n in enumerate(nums):
    print(i, n)


from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, num in enumerate(nums):
        if num == 7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    first_seven = -1
    for i, num in enumerate(nums):
        if num == 7:
            if first_seven == -1:
                first_seven = i
            else:
                return i - first_seven


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

# ZIP

"""
Python provides an easy way to iterate over multiple lists at the same time using the zip() function. 
The zip() function takes multiple lists as arguments and returns an iterator of tuples. 
Each tuple contains an element from each list.
This is useful when we have multiple lists of the same length and want to iterate over them together.
"""


names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [90, 85, 88, 92]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")


from typing import List, Dict


def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    res = {}
    for name, score in zip(names, scores):
        res[name] = score

    # or 

    # return dict(zip(names, scores))

    return res






# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))



# Inequality shorcut

"""
Python allows us to take a small shortcut when making multiple comparisons.

"""

x = 5

if 0 < x < 10:
    print('x is between 0 and 10')

from typing import List


def is_arr_valid(names: List[str], max_length: int) -> bool:
    return True if 0 < len(names) <= max_length else False



# do not modify below this line
print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 1))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 4))
