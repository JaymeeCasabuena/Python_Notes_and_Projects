def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    return arr
    # No need to 'remove' arr[i], since we already shifted

# print(removeMiddle([1, 2, 3, 4], 1, 4))

def removeDuplicates(nums):
  l = 1
  for r in range(1, len(nums)):
    if nums[r] != nums[r - 1]:
      nums[l] = nums[r]
      l += 1
  return l


def removeDuplicates(nums):
  l = 2
  for r in range(2, len(nums)):
    if nums[r] != nums[l - 2]:
      nums[l] = nums[r]
      l += 1
  return l, nums

# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


def removeElement(nums, val):
  k = 0
  for i in range(len(nums)):
    if nums[i] != val:
      nums[k] = nums[i]
      k += 1
  return k, nums

# print(removeElement([0,1,2,2,3,0,4,2], 2))

# 2, 3, 2, 3 2, 2, 3, 3

def applyOperations(nums):
  p = 0
  for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
      nums[i] *= 2
      nums[i + 1] = 0
  for r in range(len(nums)):
    if nums[r] != 0:
      nums[p] = nums[r]
      p += 1
  while p < len(nums):
    nums[p] = 0
    p += 1
  return nums


# print(applyOperations([1,2,2,1,1,0]))


# def getConcat(nums):
  
#   dup = nums.copy()
#   return [x for x in nums] + [x for x in dup]

# def getConcat(nums):
  
#   return nums + nums

def getConcat(nums):
  
  ans = []
  
  for i in range(2):
    for n in nums:
      ans.append(n)
  return ans

# print(getConcat([1,3,2,1]))

#stack


def isValid(s):
  stack = []
  parentheses_sets = {')' : '(', ']' : '[', '}' : '{'}
  for c in s:
    if c in parentheses_sets:
      #stack[-1] peek the top of the stack
      if stack and stack[-1] == parentheses_sets[c]:
        stack.pop()
      else: return False
    else: 
      stack.append(c)
  return True if not stack else False

def twoSum(nums, target):
  nums_map = {}
  for i, n in enumerate(nums):
    print(nums[i], "hello")
    if (target - n) in nums_map:
      return [nums_map[target - n], i]
    else:
      nums_map[n] = i

# print(twoSum([4,5,6], 10))

def isAnagram(s, t):
  s_map = {}
  t_map = {}

  for c in s:
    if c in s_map:
      s_map[c] += 1
    else: 
      s_map[c] = 1
        
  for c in t:
    if  c in t_map:
      t_map[c] +=1
    else: 
        t_map[c] = 1

  return True if s_map == t_map else False

# print(isAnagram("jar", "jam"))

def isPalindrome(s: str) -> bool:
        text = ''.join(char for char in s if char.isalnum()).lower()

        l, r = 0, len(text) -1

        while l < r:
            if text[l] != text[r]:
                return False
            else:
                l += 1
                r -= 1
        return True 


# print(isPalindrome("Was it a car or a cat I saw?"))


"""

# Intuition

From the description palindrome is the same forward and backward gives a clue that we need to check both ends of the given string. So what's come to mind is to use 2 pointer, which is best to use when we need to keep track of two individual elements.

So we can create two pointers, left and right then check if the character at these two pointers are the same, if the same we increment left and decrement right. We continue this until the two pointers cross. If not the same return false since it means, it is not a palindrome. 

# Approach

It says it is case insensitive and ignores all non alphanum

so first thing to do is remove all non alphanum by using join method and string manipulation 
join each char by '' (no space) then check each char if it is alphanum

after that initialize the two pointers, one starts at 0 (index 0) and last index (len(s) - 1)

then loop thru each car in the string using while loop, with a condition of l < r (l is less than r, since r would be the bigger number (index) if they're the same num it means the two pointers reached the middle or cross

lastly apply the logic I mentioned above



# Complexity
- Time complexity:

time complexity is o(n) since I check every char in the string and compare it

- Space complexity:
space comp is o(n) since I used extra memory

"""

def twoSum(numbers, target):
  l, r = 1, len(numbers) # 1 and 4

  while l < r:
    if (numbers[l - 1] + numbers[r - 1]) > target:
      r -= 1
    elif (numbers[l - 1] + numbers[r - 1]) < target:
      l += 1
    else: 
      return [l, r]

# print(twoSum([1,2,3,4], 3), "hello")

"""


# Intuition
Unlike the other 2 sum problem, the given input is sorted in non decreasing (ascending but could mean it will have duplicates)

index1 and index2 cannot be equal

There's 2 condition: there will be exactly one valid solution and  solution must use o(1) no extra memory

so hashmap is out of the question, I need to traverse the input in place. I can use two pointers to compare 2 elements to the target

# Approach


I start the left pointer at 1 and right pointer at length of input to achieve 1 indexed and we just access the actual index by substracting 1 to the pointers to get the actual element

since the input is ordered we know that the smallest number would be on the left side (start of left pointer) and largest number (last element or the start of right pointer)

we compare the sum of the values of the two pointer to the target, if it's bigger we decrement the right side since we know incrementing the left side won't make sense cos we just added the smalled and the largest numbers.

if the sum is smaller we increment the left pointer, applying the same logic

and if the sum is the same as the target we return the index




# Complexity

time is o(n) as I used two pointers to check each element

space is o(i) as I didn't use extra space

"""

def threeSum(nums):
    nums.sort() 
    res = []
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        k, j = i + 1, len(nums) - 1  
        
        while k < j:
            triplet_sum = nums[i] + nums[k] + nums[j]
            
            if triplet_sum > 0:
                j -= 1  
            elif triplet_sum < 0:
                k += 1  
            else:
                res.append([nums[i], nums[k], nums[j]])
                
                while k < j and nums[k] == nums[k + 1]:
                    k += 1
                while k < j and nums[j] == nums[j - 1]:
                    j -= 1
                
                k += 1
                j -= 1
    
    return res

# print(threeSum([-1,0,1,2,-1,-4]))


def topKFrequent(nums, k):
  frequent_nums = {}
  res = []

  for i, n in enumerate(nums):
      if n in frequent_nums and frequent_nums[n] < k:
          frequent_nums[n] += 1
      elif n in frequent_nums and frequent_nums[n] == k:
        continue
      else: 
         frequent_nums[n] = 1
      
      if n in frequent_nums and frequent_nums[n] == k:
        res.append(n)

  
  return res


print(topKFrequent([1,2,2,3,3,3], 2))







