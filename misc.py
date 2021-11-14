# def get_digit(number, n):
#     return number // 10**n % 10

# # 0th index
# get_digit(987654321, 0)
# # 1


# numbers = [4, 8, 9, 0]
# print(sorted(numbers))

# numbers_tuple = (6, 9, 3, 1)
# print(sorted(numbers_tuple))

# string_value = 'I like to sort'
# print(sorted(string_value))

# string_value = 'I like to sort'
# print( ' '.join(sorted(string_value.split(' ') )) )

# names = ['harry', 'Suzz', 'al', 'Mark']
# print(sorted(names, key = lambda x: x[-1]))

# names = ['harry', 'Suzz', 'al', 'Mark']
# print(sorted(names, key = lambda x: x[-1], reverse=True))

# # case-insensitive sorting 
# print(sorted("This is a test string from Andrew".split(), key=str.lower)) 
        
# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# print(sorted(student_tuples, key=lambda student: student[2]))

# class Student:
#     def __init__(self, name, grade, age):
#         self.name = name
#         self.grade = grade
#         self.age = age
#     def __repr__(self):
#         return repr((self.name, self.grade, self.age))

# student_objects = [
#     Student('tunde', 'Z', 10),
#     Student('john',  'A', 15),
#     Student('jane',  'B', 12),
#     Student('dave',  'B', 10),   
# ]
# print(sorted(student_objects, key=lambda student: student.age))


# from operator import itemgetter, attrgetter

# print(sorted(student_tuples, key=itemgetter(2)))
# print(sorted(student_objects, key=attrgetter('grade', 'age'))) #sort by grade, then age i.e if grade is equal, then sort by age
# print(sorted(student_tuples, key=itemgetter(1,2)))


# def sortSentence(s: str) -> str:
#     count_array = [0]  * len(s.split(' '))
#     print(len(s.split(' ')))
#     for word in s.split(' '):
#         print(word, int(word[-1])-1)
#         count_array[int(word[-1])-1] = word[:-1]
#     print(count_array)

# sortSentence("lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1")

# aResult = [[0 for j in range(0, 4)] for i in range(0, 4)]
# print(aResult)

# print(bin(157))
# print(bin(157 >> 1))
# print(bin(157 << 1))

# def factorial(n):
#     if n == 0 : return 1
#     m = factorial(n-1)
#     print(n, m)
#     return n*m


# print(factorial(1))


# https://leetcode.com/discuss/interview-question/algorithms/374846/twitter-oa-2019-university-career-fair
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended another variation
def universityCareerFair(arrival, duration):
    aux = sorted(
        list(zip(arrival, duration)),
        key=lambda p: (sum(p), p[1])
    )   
    ans, end = 0, -float('inf')
    for arr, dur in aux:
        if arr >= end:
            ans, end = ans + 1, arr + dur
    return ans
    

# print(universityCareerFair([1, 3, 3, 4, 5, 7], [2, 2, 1, 1, 2, 1])) # 4
# print(universityCareerFair([1, 2], [7, 3])) # 1
# print(universityCareerFair([1, 3, 4, 6], [4, 3, 3, 2])) # 2

def balancedSalesArray(nums):
    left, right = 0, len(nums) - 1
    sumleft, sumright = nums[left], nums[right]

    while left < right:
        if sumleft < sumright:
            left += 1
            sumleft += nums[left]
            
        elif sumright < sumleft:
            right -= 1
            sumright += nums[right]    
        else:
            left += 1
            right -= 1
            sumleft = nums[left]
            sumright = nums[right]
            
    
    return left

def pivotIndex(nums):
    # Time: O(n)
    # Space: O(1)
    left, right = 0, sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num
   
    return -1

# print(pivotIndex([1, 7, 3, 6, 5, 6]))
# print(pivotIndex([0, -1, 1])) #edge case --> algo takes into account all prefix before every index

# print(balancedSalesArray([1, 7, 3, 6, 5, 6]))
# print(balancedSalesArray([0, -1, 1])) #wrong


# print(balancedSalesArray([1, 2, 3, 4, 1, 2, 3]))
# print(balancedSalesArray([1, 2, 3, 3]))
# print(balancedSalesArray([1, 2, 3, 4, 6]))
# print(balancedSalesArray([6, 1, 2, 3, 4]))


def reverseString(self, s) -> None:

    size = len(s)
    
    # reverse string by mirror image
    for i in range(size//2):
        s[i], s[-i-1] = s[-i-1], s[i]

def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("here")
        return
        # print("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        print(step, i)

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)

# permutations("ABC")

def kthGrammar( n: int, k: int) -> int:
    def replace(symbol):
        
        map = {'0': '01', '1': '10'}
        sym = ''
        for char in str(symbol):
            sym += map[char]
        return sym
        
            
    if n == 1:
        return 0
    return replace(kthGrammar(n-1, k-n))

   
    

# print(kthGrammar(3,4))
events = [[1,10],[2,2],[2,2],[2,2],[2,2]]
aux = sorted(events, key = lambda x: (x[1], x[0]) )
# print(aux)

import heapq
def maxEvents(events):
        # sort according to start time
        events = sorted(events)
        total_days = max(event[1] for event in events)
        min_heap = []
        day, cnt, event_id = 1, 0, 0
        while day <= total_days:
            # if no events are available to attend today, let time flies to the next available event.
            if event_id < len(events) and not min_heap:
                day = events[event_id][0]

            # all events starting from today are newly available. add them to the heap.
            while event_id < len(events) and events[event_id][0] <= day:
                heapq.heappush(min_heap, events[event_id][1])
                # print(events[event_id][1])
                event_id += 1

            # if the event at heap top already ended, then discard it.
            while min_heap and min_heap[0] < day:
                # print("here", day)
                # print("here", min_heap[0])
                heapq.heappop(min_heap)

            # attend the event that will end the earliest
            if min_heap:
                heapq.heappop(min_heap)
                cnt += 1
                print(cnt)
            elif event_id >= len(events):
                break  # no more events to attend. so stop early to save time.
            day += 1
        return cnt

maxEvents([[1,2],[1,2],[1,2],[2,3],[3,4]])


def canBeSplit(nums):
    map = {}

    for i in range(len(nums)):
        num = nums[i]
        if num not in map:
            map[num] = 1
        else:
            map[num] = map[num] + 1
    
    for k, v in map.items():
        if v %2 != 0:
            return False
    
    return True



print(canBeSplit([-1,2,2,-1]))