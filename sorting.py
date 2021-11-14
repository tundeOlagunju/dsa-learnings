
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
    mergesort(right)
    mergesort(left)
    merge(right, left) # merge two sorted list


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
        return r # parttition index
   
    def quicksort(start, end):
        if start >= end: return
        p_index = partition(start, end)
        quicksort(start, p_index - 1)
        quicksort(p_index + 1, end)
    
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
print(nums)

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


