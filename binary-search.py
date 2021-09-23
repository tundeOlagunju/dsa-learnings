
# Test your binary search with 2 elements to see if it terminates

# This approach works but when you have duplicates, it does not return the lowest index that is equal to your target, compare this with 
# binary search 4 which follows the "Best template ever". This form of binary search can also be modified to find the last index or first index 
# of the target as required
def binary_search(list, target):
    hi = len(list) - 1
    low = 0

    while hi >= low:
        mid = (hi + low)//2 # Integer overflow is not possible in python
        guess = list[mid]
        if guess == target:
            return mid
        elif guess > target:
            hi = mid - 1 # Note how hi >= low
        else: low = mid + 1
    
    return -1

# modifying it to return the first index of target
def binary_search_7(list, target):
    hi = len(list) - 1
    low = 0
    result = -1

    while hi >= low:
        mid = (hi + low)//2 # Integer overflow is not possible in python
        guess = list[mid]
        if guess == target:
            result = mid
            hi = mid - 1
        elif guess > target:
            hi = mid - 1 # Note how hi >= low
        else: low = mid + 1
    
    return result

# modifying the first template to return the last index of the target if there are duplicates
def binary_search_5(list, target):
    hi = len(list) - 1  
    low = 0
    result = -1

    while hi >= low:
        mid = (hi + low)//2 # Integer overflow is not possible in python
        guess = list[mid]
       
        if guess == target:
            # because nothing before mid
            # can be the last occurance of target.
            # maybe mid is the last occurance , maybe not
            # so let's narrow the target for [mid+1...high] and find  
            result = guess
            low = mid + 1

        elif guess < target:
            low = mid + 1
        else: 
            hi = mid - 1
        
    return result


# def binary_search_2(list, target):
#     hi = len(list)
#     low = 0

#     while hi > low:
#         mid = (hi + low)//2 # Integer overflow is not possible in python
#         guess = list[mid]
#         if guess == target:
#             return guess
#         elif guess > target:
#             hi = mid # Note how hi > low
#         else: low = mid + 1
    
#     return None


# def binary_search_3(nums, target):

#     left, right = 0, len(nums)
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             print("here mid")
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid

# # this part is unneccessary unless right = len(nums) - 1, if right = len(nums), it's unnecessary
#     # Post-processing:
#     # End Condition: left == right
#     # if left != len(nums) and nums[left] == target:
#     #     print("here")
#     #     return left
#     return -1

# this template is only used when we are sure that number is within search space(not necessarily), follows the "Best template ever"
def binary_search_4(list, target):
    hi = len(list) - 1  
    low = 0

    while hi > low:
        mid = (hi + low)//2 # Integer overflow is not possible in python
        guess = list[mid]
        if guess >= target:
            hi = mid # Note how hi > low
        else: low = mid + 1
    
    return low  # minimum index value that satisifes the condition in this case (even if there are dupliactes): guess >= target



# Best template ever
# Learn this, in most cases used for minimum value that satisfies the condition. Answer is always within the search space
# def binary_search(array) -> int:
#     def condition(value) -> bool:
#         pass

#     left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
#     while left < right:
#         mid = left + (right - left) // 2
#         if condition(mid):
#             right = mid
#         else:
#             left = mid + 1
#     return left



# https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
# returns the last index of the target if there are duplicates
# the condition is the minimum value that satisfies array[mid+1] > target condition(which means the first number after mid greater than target )
def binary_search_6(array, target) -> int:
    def condition(value) -> bool:
        return array[value] > target

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left - 1


list = [-1,0,1,2,3,4,5,6,7]
list2 = [1,2,3,4,5,6,7]
list3= [1,2,2,2,3,4]
print(binary_search_6(list3, 3))



# from collections import defaultdict

# dict_default = defaultdict(int)

# print(dict_default["key1"])




