import time
import random

def linearSearch(list1, item):
  for i in range(len(list1)):
    if item==list1[i]:
      return True
  return False

def binSearchIter(lst, item):
  low, high = 0, len(lst) - 1
  
  if (high < 0): # edge case where lst is empty
    return False

  while (low < high):
    mid = (high + low) // 2
    x = lst[mid]
    
    if (x == item):
      return True
    elif (x < item): # cannot be on left side
      low = mid + 1
    else: # x > item, cannot be on right side
      high = mid - 1
  return lst[low] == item

nums = []
for i in range(10000):
  nums.append(random.randint(0,10000))
nums.sort()

startLin=time.time()
for i in range(10000):
  item = random.randint(0,10000)
  linearSearch(nums,item)
endLin = time.time()

startBin = time.time()
for i in range(10000):
  item = random.randint(0,10000)
  binSearchIter(nums, item)
endBin = time.time()

print("Linear search took " + str(round(endLin-startLin, 2)) + " seconds.")

print("Binary search took " + str(round(endBin-startBin, 2)) + " seconds.")