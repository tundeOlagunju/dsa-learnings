
# Test your binary search with 2 elements to see if it terminates

# This approach works but when you have duplicates, it does not return the lowest index that is equal to your target, compare this with 
# binary search 4 which follows the "Best template ever". This form of binary search can also be modified to find the last index or first index 
# of the target as required
def binary_search(list, target):
    hi = len(list) - 1
    low = 0

    while hi >= low:
        mid = (hi + low)//2 # Integer overflow is not possible in python #bracket is compulsory
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

print(binary_search_4([1,2,3,4,5,5,5,5], 5))

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
# print(binary_search_6(list3, 3))



# from collections import defaultdict

# dict_default = defaultdict(int)

# print(dict_default["key1"])

# In these two cases, we are sure the target is in the array (even if the target is not in the array, we just check if nums[lo] == target else we return -1), we just reduce the search space intuitively to ensure we get the first occurence or last occurrence of the target
# This gets the index of the last bad version e,g https://leetcode.com/problems/furthest-building-you-can-reach/solution/
def binary_search_10(list, target):
    hi = len(list) - 1  
    low = 0

    while hi > low:
        mid = (hi + low + 1 )//2  #upper middle since we want the last occurrence when odd, return the only mid. when even, return the upper mid.  if you use uppermid, try asmuch as possible to use hi = mid - 1
        guess = list[mid]
        if guess <= target:
            low = mid 
        else: hi = mid - 1 
    return low if list[low] == target else -1   

print(binary_search_10([0,1,1,2,3,4,5,5,5,5], 1))


# https://leetcode.com/problems/search-insert-position/discuss/423166/Binary-Search-101
# This gets the index of the first bad version. We are sure the target is in the array. https://leetcode.com/problems/first-bad-version/solution/
def binary_search_11(list, target):
    hi = len(list) - 1  
    low = 0

    while hi > low:
        mid = (hi + low)//2  #lower middl.when odd, return the only mid. when even, return the lower mid. if you use lowermid, try asmuch as possible to use lo = mid + 1
        guess = list[mid]
        if guess >= target:
            hi = mid     
        else: low = mid + 1 
    return low  

print(binary_search_11([0,1,1,2,3,4,5,5,5], 1))



from bisect import bisect_left, bisect_right, bisect


def searchRange(self, nums, target: int):
    start = bisect_left(nums, target)
    if start >= len(nums) or nums[start] != target:
        return [-1, -1]
    return [start, bisect_right(nums, target) - 1]  #first bad version and last bad version? are you sure? read Find First and Last Position of Element in Sorted Array, omo it is o




# The short rule to remember is: if you used hi = mid - 1, then use the higher midpoint. If you used lo = mid + 1, then use the lower midpoint. If you used both of these, then you can use either midpoint. If you didn’t use either (i.e., you have lo = mid and hi = mid), 
# then, unfortunately, your code is buggy, and you won’t be able to guarantee convergence.
# higher midpoint = lo + hi +1/2
#lower midpoint = lo + hi /2


# Binary serach applications 

# find the first index of an element in a list -> first bad version (list with dups)
# find the last index of an element in a list -> last bad version (list with dups)
# Find First and Last Position of Element in Sorted Array -> same as first 2 , we can also use Bisect left and right in Python

# find the greatest key lesser than or equal a particular value -> similar to treemap in java (floorKey)
# find the least key greater than or equal to a particular value -> similar to treemap in java (ceilingKey)


# Find the magic index. A magic index is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find the magic index if one exists in the array A. Follow UP -> What if the elements are not distinct?


#greatest key lesser than or equal to target (floorKey) tbh I am not expecting duplicate in the array because even treemap would not have duplicates
def binary_search_12(nums, target):
    # lo , hi = 0, len(nums) - 1

    # while lo < hi:
    #     mid = (lo + hi + 1)//2 #upper mid here because we are looking for the greatest key 
    #     guess = nums[mid]

    #     if guess > target:
    #         hi = mid - 1
    #     else: lo = mid
    
    # return nums[lo] if nums[lo] > target else None
    
    # with bisect_right , this is actually not that easy to figure out
    start = bisect_right(nums, target + 1) - 1
    if start < 0 or nums[start] > target: return None
    return nums[start] 

# print(binary_search_12([1,2,3,4,10,11,12], -1))


#find the least key greater than or equal to a particular value,tbh I am not expecting duplicate in the array because even treemap would not have duplicates
def binary_search_13(nums, target):
    # lo , hi = 0, len(nums) - 1

    # while lo < hi:
    #     mid = (lo + hi )//2 #lower mid here because we are looking for the least key 
    #     guess = nums[mid]

    #     if guess >= target:
    #         hi = mid
    #     else: lo = mid + 1
    
    # return nums[lo] if nums[lo] >= target else None
    
    # with bisect_left , this is actually not that easy to figure out
    start = bisect_left(nums, target)
    if start >= len(nums) or nums[start] < target: return None
    return nums[start]


# print(binary_search_13([1,2,3,4,10,11,12], 100))


#no dups
def magicIndex1(nums):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        
        if nums[mid] > mid:
            hi = mid - 1
        elif nums[mid] < mid:
            lo = mid + 1
        else: return mid
    
    return -1

def magicIndexRecursive(nums):

    def magicIndex(lo, hi):
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        if nums[mid] > mid: return magicIndex(lo, mid - 1)
        elif nums[mid] < mid: return magicIndex(mid + 1, hi)
        else: return mid
    
    return magicIndex(0, len(nums) - 1)

# print(magicIndexRecursive([-40,-20,-1,1,2,3,5,7,9,12,13]))


#with dups (not trivial) 
def magicIndex2(nums):

    def magicIndex(lo, hi):
        if lo > hi: return -1

        midIndex = (lo + hi) // 2
        midValue = nums[midIndex]

        if midValue == midIndex:
            return midIndex

        # since we cant make any conclusive decision whether the magicIndex is on the right or left for arrays with dups, we have to search both left and left

        #Search left -> where should we start searching the left from, can we cut out some unnecessary things to search? 
        #if the midValue is less than the midIndex - 1, we are 100% sure that midIndex - 1 cannot be the magicIndex because for it to be the magicIndex, arr[midIndex - 1] must be midIndex - 1, but it cannot be since midValue is already less than midIndex - 1 and the array is in increasing order

        left = -1
        if midValue < midIndex - 1:
            left = magicIndex(lo, midValue)
        else: left = magicIndex(lo, midIndex - 1)

        if left >= 0: return left

        #Search right
        right = -1
        if midValue > midIndex + 1:
            right = magicIndex(midValue, hi)
        else: right = magicIndex(midIndex + 1, hi)

        return right
    
    return magicIndex(0, len(nums) - 1)

print(magicIndex2([-10,1,1,1,1,1,2,3,4,5,6,7,8]))


#Binary search does not even require all the elements of an array to be sorted. It could also be valid when 
#parts of the array is sorted if we can guess the part of the array the target will be located
#[4,5,6,7,0,1,2]
#[10,15,20,0,5] #left side ordered to mid
#[50,5,20,30,40] #right side ordered from mid
#non-distinct elements
#[2,2,2,3,4,2] if the left and mid element are the same, if the rightmost element is diff, we can just search right side
#else, we have no option than to search both sides
#[2,2,2,2,3,4,5,6]
def searchRotatedSortedArray(nums, target):

    def search(lo, hi):
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] < nums[mid]: #left side ordered to mid
            if target >= nums[lo] and target < nums[mid]: 
                return search(lo, mid - 1) #search left
            else: return search(mid + 1, hi) #search right
        elif nums[lo] > nums[mid]: #right side ordered from mid
            if target > nums[mid] and target <= nums[hi]:
                return search(mid + 1, hi) #search right
            else: return search(lo, mid - 1) #search left
        elif nums[lo] == nums[mid]: #what do you do when left and mid are identical 
            if nums[hi] != nums[mid]:
                return search(mid + 1, hi) #search right
            else:
                res = search(lo, mid - 1)
                if res == -1: return search(mid + 1, hi) 
                else: return res
    return search(0, len(nums) - 1)
            




       
    

