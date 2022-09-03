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
    
print('here')
print(universityCareerFair([1, 3, 3, 4, 5, 7], 
                           [2, 2, 1, 1, 2, 1])) # 5

print(universityCareerFair([1, 2, 3], [9, 1, 1])) # 2

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

import collections
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

# maxEvents([[1,2],[1,2],[1,2],[2,3],[3,4]])


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



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findValidDiscountCoupons' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY discounts as parameter.
#

def findValidDiscountCoupons(discounts):
    output=[]
    def isValid(discount, first, last, checked):
        if discount[first] == discount[last]: return True
        for i in range(first, len(discount), 2):
            if i+1 < len(discount):
                if discount[i] != discount[i+1]:
                    if checked < 2:
                        checked+=1
                        isPalindrome(discount, i, last, checked)                 
                    else: return False           
        return True
        
    
    def isPalindrome(discount, first=None, last=None, checked = 0):
        if not first: first = 0
        if not last:  last  = len(discount) - 1
        while first >= 0 and last < len(discount) and first <= last and discount[first] == discount[last]:
            first += 1
            last -= 1
        if discount[first] == discount[last]:
            return True
        else:
            if checked < 2:
                checked += 1 
                isValid(discount, first, last, checked)
            else: return False
        
    for discount in discounts:
        if not discount: 
            output.append(1)
            continue
        # if len(discount) > 2 and discount[0] == discount[-1]:
        #     first = discount[0]
        #     last = discount[-1]
        #     discount = discount[1:len(discount)-1]
 
        if isPalindrome(discount):
            # if first == last:
            output.append(1)
            # else: output.append(0)
        else: output.append(0)
    
    return output
        
        
        
    

# def permute(l):
#     def dfs(path, used, res):
#         if len(path) == len(l):
#             res.append(path) # note [:] make a deep copy since otherwise we'd be append the same list over and over
#             return

#         for i, letter in enumerate(l):
#             # skip used letters
#             if used[i]:
#                 continue
#             # add letter to permutation, mark letter as used
#             path.append(letter)
#             used[i] = True
#             dfs(path, used, res)
#             # remove letter from permutation, mark letter as unused
#             path.pop()
#             used[i] = False
        
#     res = []
#     dfs([], [False] * len(l), res)
#     return res

# print(permute([1,2,3]))




#     public List<String> generateParenthesis(int n) {
#         List<String> res = new ArrayList<String>();
#         dfs(res, new StringBuilder(), 0, 0, n);
#         return res;
#     }

#     private void dfs(List<String> res, StringBuilder sb, int open, int close, int n) {
#         if (sb.length() == 2 * n) {
#             res.add(new String(sb));
#             return ;
#         }

#         if (open < n) {
#             sb.append("(");
#             dfs(res, sb, open + 1, close, n);
#             sb.deleteCharAt(sb.length() - 1);
#         }
#         if (close < open) {
#             sb.append(")");
#             dfs(res, sb, open, close + 1, n);
#             sb.deleteCharAt(sb.length() - 1);
#         }
#     }
# }



logData = [['123 234 456']]
for row in logData:
    # print(row)
    s = ''.join(row)
    print(s)

print(''.join(['a']))


def hackerCards(collection, d):
    collection = set(collection)
    res = []
    curSum = 0
    # Write your code here
    for i in range(1, d + 1):
        if i not in collection and curSum + i <= d:
            curSum += i
            res.append(i)
    return res


# print(hackerCards([1,3,4], 7))

# print( [[0]*5 for i in range(5)])
# print( [[0 for _ in range(5)] for _ in range(5)])

# print([[False for _ in range(5)] for i in range (4)])

q= collections.deque([(1,2)])
while q:
    c= q.popleft()
    # print(c)


nums = [1,2,3,4]

for i in range(len(nums)):
    for j in range(i+1, len(nums)+1):
        for k in range(i, j):
            # print(k)
            print(nums[k], end="")
        print()



class Chain:
  def __init__(self,name,freq):
    self.name = name
    self.freq = freq

    # def __lt__(self, other):
    #     if self.label == other.label:
    #         return self.cost > other.cost

    # def __eq__(self, other: object) -> bool:
    #     return self.label  == other.label and self.cost == other.cost



# arr = [Chain("Tunde", 2), Chain("Yemi", 2), Chain("Yemi", 3), Chain("Bolu", 2), Chain("Bolu", 3)]
# for i in (sorted(arr, key= lambda x: (x.name, x.freq) ,reverse = True)):
#     print(i.name, i.freq)



def find_grants_cap(grantsArray, newBudget):
  """
  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190
  
  [2, 47, 47, 47, 47] ans = 47
  
  [2, 50, 100, 120, 1000]
  
  [38, 38, 38, 38, 38]
  
  2 < 38: (38 - 2) = 36/4 = 9
  
  [2, 47, 47, 47, 47]

  [2, 4] n
  """
  
  grantsArray.sort()
  cap = float(newBudget) / float(len(grantsArray))
  print(cap)
  
  for i, grant in enumerate(grantsArray):
    if grant <= cap:
      cap = cap + float((cap - grant)) / float((len(grantArray) - 1) - i)
    
    else: return cap




#sort string
string = "Tunde"
''.join(sorted(string))

# values of dictionary as list
map = {'a': 'b', 'c': 'd'}
list(map.values())

# extract dictionary single key-value pair in variables
d = {'a': 1}
[(k, v)] = d.items()
print(k, v)


numbers = [1,2,3,4,5,6,7,7]

def check_even(number):
    return number % 2 == 0

even_numbers = list(filter(check_even, numbers))
even_numbers_2 = list(filter(lambda x: (x%2 == 0), numbers))
print(even_numbers_2)

def check_odd(x):
    return (x % 2) == 0

# l1 = list(range(1,20))
# l2 = list(filter((lambda x:x>=5 and check_odd(x)), l1))
# print(l2)

def even_and_greater5(x):
    return (x % 2) == 0 and x >= 5

l1 = list(range(1,20))
l2 = list(filter(even_and_greater5, l1))
print(l2)



# This post is in continuation of Online Assessment Test post (https://leetcode.com/discuss/interview-question/838686/yelp-oa-2020-filter-the-businesses-and-return-ordered-list/696180).

# Interview Round 1

# Problem :
# Given a list of business_names (strings) and a searchTerm (string).
# Return a list of business_names that contains searchTerm as prefix in the business_names.

# E.g.
# Example 1.
# Input:

# business_names[] = { "burger king", "McDonald's", "super duper burger's", "subway", "pizza hut"}
# searchTerm = "bur"
# Ouput:
# ["burger king", "super duper burger's"]

# Example 2
# Input:

# business_names[] = { "burger king", "McDonald's", "super duper burger's", "subway", "pizza hut"}
# searchTerm = "duper bur"
# Ouput:
# ["super duper burger's"]

# Expected to discuss the approach and implement the solution.
# (Allowed to run and debug the code as many times as we want, in order to make it error free)





# businesses = [
#     {'vegan_only': True, 'price': 100, 'distance': 50},
#     {'vegan_only': False, 'price': 100 }
# ]

class TrieNode:
    def __init__(self):
        self.word = None
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)


class Solution:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True
        curr.word = word
    
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children
        return curr.is_word
    
    def prefix(self, pref):
        curr = self.root
        for char in pref:
            if char not in curr.children:
                return False
            curr = curr.children
        return True

    

business_names = ["McDonald's", "super duper burger's", "subway", "pizza hut", "burger king", "burrister", "fgbur", "burhiger", "Paul"]
searchTerm = "bur"

#names that start with bur
#names that has bur in them
#names without any

def compare(item1, item2):
    
    if item1.startswith(searchTerm) and not item2.startswith(searchTerm):
        return -1
    if not item1.startswith(searchTerm) and item2.startswith(searchTerm):
        print(item1, item2)
        return 1
    if searchTerm in item1 and not searchTerm in item2:
        return -1
    if searchTerm in item2 and not searchTerm in item1:
        return 1
    return 0


from functools import cmp_to_key


print(sorted(business_names, key=cmp_to_key(compare)))

