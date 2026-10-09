# Simple search it's O(n) we iterate through all elements to find the wanted one.
import time
nums_list = [23,32,46,55,67,99,105]
wanted_num = 55
exist = 0

# Simple Search
# start_time = time.perf_counter()
# for i, num in enumerate(nums_list):
#   if num == wanted_num:
#     exist += 1
#     print(f"number {wanted_num} founded at position: {i}")
#     break
# if exist == 0:
#   print(f"number {wanted_num} not founded")
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Execution time for simple Search: {elapsed_time:.6f} seconds")
 
# Binary search is the technique that make search in the half of the list O(log(n)) it works because the list is already ordred


def binary_search(list, wanted):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]

    if guess == wanted:
      return f"number founded at {mid} index"
    elif guess < wanted:
      low = mid + 1
    else:
      high = mid - 1

  return f"{wanted} not found"

# start_time2 = time.perf_counter()
# print(binary_search(nums_list, 55))
# end_time2 = time.perf_counter()

# elapsed_time2 = end_time2 - start_time2
# print(f"Execution time Binary Search: {elapsed_time2:.6f} seconds")

  
nums = [0,1]

def missing_number(nums):
  actual_sum = 0
  expected_sum = 0
  expected_sum = len(nums)*(len(nums) + 1) // 2
  for i in range(len(nums)):
    actual_sum += nums[i]
  return expected_sum - actual_sum
    

print(missing_number(nums))