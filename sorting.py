
# def selection_sort(list):

#     # for i in range(len(list)):
#     #     min_index = i
#     #     for j in range(i+1, len(list)): 
#     #         if list[j] < list[min_index]:
#     #             min_index = j
#     #     list[i], list[min_index] = list[min_index], list[i]

#     # less efficient, extra space
#     for i in range(len(list)):
#         minimum = min(list[i:])
#         list[list.index(minimum)], list[i] = list[i], list[list.index(minimum)]
    


# L = [3, 1, 1, 41, 59, 26, 53, 59, 0]
# selection_sort(L)
# print(L)

# NlogN extra space here, this can be rewritten to use N space
def mergesort(list):
    def merge(right, left):
        i = j = k = 0
        while i < len(right) and j < len(left):
            if right[i] <= left[j]:
                list[k] = right[i]
                i += 1
            else:
                list[k] = left[j]
                j += 1
            k += 1
        
        while i < len(right):
            list[k] = right[i]
            i += 1
            k += 1
        
        while j < len(left):
            list[k] = left[j]
            j += 1
            k += 1
    if len(list) < 2:
        return
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    mergesort(left) #sort left T(N/2)
    mergesort(right) #sort right T(N/2)
    merge(right, left) # merge two sorted list T(N) => N work at each level (log N levels), NlogN


# list = [23,4,1,3,1]
# mergesort(list)
# print(list)

import random
def quicksort(list):
    def partition(start, end):
        pivot = list[start] # lets start with the first element as the pivot and start as partitionIndex
        l = start + 1 
        r = end
        while l <= r:
            while l<=r and list[l] < pivot: l += 1
            while l<=r and list[r] > pivot: r -= 1
            if l <= r:
                list[l], list[r] = list[r], list[l]
                l += 1
                r -= 1
        list[start], list[r] = list[r], list[start]
        return r # parttition index which tells us which element is in position
   
    def quicksort(start, end):
        # shuffle the array
        if start >= end: return
        p_index = partition(start, end) #since we know the P_index(which is the element in the right position)
        quicksort(start, p_index - 1) #sort its right part and then
        quicksort(p_index + 1, end)#its left 
    
    quicksort(0, len(list) - 1)

# without keeping track of partition index buggy???
def quicksort2(nums):
    def helper(head, tail):
        if head >= tail : return
        l, r = head, tail
        pivot = nums[(r+l)//2]
        while l <= r:
            while l<=r and nums[l] < pivot: l += 1
            while l<=r and nums[r] > pivot: r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        helper(head, r)
        helper(l, tail)

    random.shuffle(nums) # guarantees performance
    helper(0, len(nums) - 1)


# list = [23,4,1,3,1]
# quicksort(list)
# print(list)

# # crude way
def quicksort(list):
    if len(list) < 2:
        return list

    pivot = list[0]
    greater = [i for i in list[1:] if i >= pivot]
    lesser = [i for i in list[1:] if i < pivot]
    return quicksort(lesser) + [pivot]+ quicksort(greater)


# print(quicksort([23,4,1,3,1]))


# Counting sort is suitable for arrays with close range 
# unstable version but in place
def countsort(nums):
    l = max(nums) + 1
    count_array = [0] * l
    for i in range(len(nums)):
        count_array[nums[i]] += 1
    
    index = 0
    for num, count in enumerate(count_array):
        while count > 0:
            nums[index] = num
            index += 1
            count -= 1

nums = [1, 0]
countsort(nums)
# print(nums)

# stable version but not in place
def countsortstable(nums):
    sorted = []
    l = max(nums) + 1
    count_array = [0] * l
    for i in range(len(nums)):
        count_array[nums[i]] += 1

    # modifying count_array to get the nest_index_array
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    
    for i in reversed(range(1, len((count_array)))):
        count_array[i] = count_array[i - 1]
    count_array[0] = 0

    # this step ensures countsort is stable, take each element in the input array, look at the modified count_array(or next_start index array)
    # and compute the position the element should go to in the sorted array. Dont also forget to increment the value in that next_start index array 
    # to cater for the next duplicated element
    for i, num in enumerate(nums):
        sorted.insert(count_array[num], num)
        count_array[num] += 1

    
    for i in range(len(sorted)):
        nums[i] = sorted[i]

# nums = [1, 0, 3, 1, 3, 1]
# countsortstable(nums)
# print(nums)



# Radix sort uses counting sort as a sub routine to sort the numbers bit by bit starting from the MSB
def radix_sort(nums):
    def countingsort(j):
        sorted = []
        count_array = [0] * 10
        for i in range(len(nums)):
            count_array[(nums[i] // 10**j ) % 10] += 1
       
        for i in range(1, 10):
            count_array[i] += count_array[i - 1]
        
        for i in reversed(range(1, len((count_array)))):
            count_array[i] = count_array[i - 1]
        count_array[0] = 0
        
        for i, num in enumerate(nums):
            sorted.insert(count_array[(num //10**j) % 10], num) #insert misbehaves, be casreful
            count_array[(num//10**j) % 10] += 1

        for i in range(len(sorted)):
            nums[i] = sorted[i]

    largest = max(nums)
    j = 0
    while largest > 0:
        largest = largest//10
        countingsort(j)
        j += 1
        
      
    
# nums = [123, 145, 166, 112, 999, 10000, 445, 567]
# radix_sort(nums)
# print(nums)


def countSort(nums):
    x = max(nums) + 1
    countArray = [0] * x


    for num in nums:
        countArray[num] += 1
    
    
    
    index = 0
    for i, count in enumerate(countArray):
        for _ in range(count):
            nums[index] =  i
            index += 1


    # print(nums)


countSort([1,2,3,4,1])



#Learn sorted in python with key argument
"""
How it works, the function passed to the key is called on every element in the input but the output does not modify
the original input.
"""
#custom function
def cast(str_num):
    return int(str_num)

values_to_cast = ['1', '2', '3', '44', '4']
sorted(values_to_cast, key = cast)

def reverse_word(word):
    return word[::-1]

sorted(['banana', 'pie', 'Washington', 'book'], key=reverse_word)

#you can use lamda instead (for simple functions) which will execute just like a function
sorted(['banana', 'pie', 'Washington', 'book'], key=lambda x: x[::-1])
sorted(values_to_cast, key=lambda x: int(x))

#inbuilt function
sorted(values_to_cast, key = int)
sorted(['al', 'harry', 'Mark', 'Suzy'], key=str.lower)
sorted(['al', 'harry', 'Mark', 'Suzy'], key=len)

#Difference between sorted and sort
"""
sort() returns None and modifies the values in place
sort is a method of the list class and can only be used with lists. It is not a built-in with an iterable passed to it.
"""

"""
Given a special alphabet (alien dictionary?) sort a list of words in ascedning order alphabetically:

alphabet: "a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"

Input: "ddr",  "nah", "dea", "dd", "ngah"

Output: "dea", "dd", "ddr", "ngah", "nah"
"""

welsh_alphabet = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]

def sort_welsh(words):
    
    token_weight = {welsh_alphabet[i]: i for i in range(len(welsh_alphabet))}
    
    def sort_by_index(word):
        ordered = []
        i = 0
        # Special charaters are
        # "ch", "dd", "ff", "ng", "ll", "ph", "rh", "th"

        while i < len(word):
            if word[i:i+2] in token_weight:
                ordered.append(token_weight[word[i:i+2]])
                i += 1
            else:
                ordered.append(token_weight[word[i]])
            i += 1
        print(ordered)
        return ordered

    return sorted(words, key=sort_by_index)

print(sort_welsh(["ddr",  "nah", "dea", "dd", "ngah"])) #mapped (but not modified) to this technically [5, 20] [16, 0, 11] [4, 6, 0] [5] [10, 0, 11] and sorted

# print(sorted( [[25, 20], [16, 0, 11]] ) )




def sort_english(words):
    
    def sort_by_index(word):
        return [ord(c) - ord('a') for c in word]

    return sorted(words, key=sort_by_index)

# print(sort_english(["ddr", "ddf", "nah"]))

# print(sorted( [ ["ABC", "DFG"], ["JFK", "IJK"] , ["JFK"] ]))

# print(sorted([[10, 20], [10, 5]]))


#Kth smallest -> Oth index, can be modified for Kth largest by manipulating k
class Solution:
    def findKthLargest(self, nums, k) -> int:
        
        def partition(high, low):
            pivot = nums[low]
            pivotIndex = low
            start = low + 1
            end = high
            
            while start <= end:
                while start <= end and nums[start] <= pivot: start += 1
                while start <= end and nums[end] > pivot: end -= 1
                
                if start <= end:
                    nums[start], nums[end] = nums[end], nums[start]
                    end -= 1
                    start += 1
            
            nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
            return end
        
        if not nums: return -1
        
        low = 0
        high = len(nums) - 1
        
        random.shuffle(nums) #shuffle element to guarantee O(N) 
        
        while low < high:
            partitionIndex = partition(high, low) #all elements to the left of partition Index are lesser than it, right -> greater     
            
            if partitionIndex == k:
                return nums[partitionIndex]
            elif partitionIndex > k:
                high = partitionIndex - 1
            else: low = partitionIndex + 1
        
        return nums[k]
    
    
    #Time complexity -> the first partioning takes N work, the next one takes N/2, tehn N/4, then N/8 ...1 = N + N/2 + N/4 +N/8 ... 1 = 2N (similar to amortized TC analysis), Note: this is true if our partitioning logic partitions the array into equal halves (balanced tree), which is why we shuffle which guarantees almost surely the worst case would not happen. The worst case is O(N^2)
    #therefor TC = O(N)
    #SC = O(1)

    #Merge sort SC explanation
#     Although each call to mergeSort triggers two recursive calls, so it makes sense to talk about and draw the binary tree of recursive calls, only one of those two recursive calls is performed at a time; the first call ends before the second call starts. Hence, at any given time, only one branch of the tree is being explored. The "call stack" represents this branch.

# The depth of the recursion tree is at most log(n), therefore the height of the call stack is at most log(n).

# How much memory does it take to explore one branch? In other words, how much memory is allocated on the call stack, at most, at any given time?

# At the bottom of the call stack, there is an array of size n.

# On top of that is an array of size n/2.

# On top of that is an array of size n/4.

# Etc...

# So the total size of the call stack is at most n + n/2 + n/4 + ... < 2n.

# Hence the total size of the call stack is at most 2n.


names = ['harry', 'Evelyn']
#sort by last character

sorted_names = sorted(names, key = lambda x: x[-1])
print(sorted_names)

print(sorted('tunde'))


print(sorted(names, key = str.lower))

def lower(c):
    return c.lower()

print(sorted(names, key = lower))


# https://stackoverflow.com/questions/25815377/sort-list-by-frequency

print(sorted(["123", "19", "15"], key = int))
#if you are afraid the int will overflow such as in Java cases like ["28287838938383389393", "7373836372727878738378"]
print(sorted(["123", "156", "19", "15"], key = lambda string: (len(string), [int(char) for char in string]))) 
print(sorted(["123", "156", "19", "15"], key = lambda string: (len(string), string))) #sort by length else use natural order

class StringNum:
    def __init__(self, string):
        self.string_num = string
    
    def __lt__(self, other):
        if len(self.string_num) == len(other.string_num):
            return self.string_num < other.string_num
        return len(self.string_num) < len(other.string_num)

d = (sorted([StringNum("123"), StringNum("156"), StringNum("19"), StringNum("15")]))
print([x.string_num for x in d ])

