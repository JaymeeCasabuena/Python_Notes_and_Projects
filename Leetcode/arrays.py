def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    return arr
    # No need to 'remove' arr[i], since we already shifted

print(removeMiddle([1, 2, 3, 4], 1, 4))

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

print(getConcat([1,3,2,1]))