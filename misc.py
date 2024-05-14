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



class Chain(object):
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq

    # def __eq__(self, other):
    #     return self.name  == other.name and self.freq == other.freq

    
    def __lt__(self, other):
        # if self.label == other.label:
        if self.freq == other.freq:
            return self.name < other.name
        return self.freq < other.freq


arr2 = [Chain("Tunde", 2), Chain("Yemi", 2), Chain("Yemi", 3), Chain("Bolu", 2), Chain("Bolu", 3)]
d = sorted(arr2)
# print([(c.name, c.freq) for c in d])
# for i in (sorted(arr, key= lambda x: (x.name, x.freq) ,reverse = True)):
#     print(i.name, i.freq)


class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank < other.rank

hand = [Card(10, 'H'), Card(2, 'h'), Card(12, 'h'), Card(13, 'h'), Card(14, 'h')]
hand_order = [c.rank for c in hand]  # [10, 2, 12, 13, 14]

hand_sorted = sorted(hand)
hand_sorted_order = [(c.rank, c.suit) for c in hand_sorted]  
print(hand_sorted_order)


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
      cap = cap + float((cap - grant)) / float((len(grantsArray) - 1) - i)
    
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
# print(k, v)


numbers = [1,2,3,4,5,6,7,7]

def check_even(number):
    return number % 2 == 0

even_numbers = list(filter(check_even, numbers))
even_numbers_2 = list(filter(lambda x: (x%2 == 0), numbers))
# print(even_numbers_2)

def check_odd(x):
    return (x % 2) == 0

# l1 = list(range(1,20))
# l2 = list(filter((lambda x:x>=5 and check_odd(x)), l1))
# print(l2)

def even_and_greater5(x):
    return (x % 2) == 0 and x >= 5

l1 = list(range(1,20))
l2 = list(filter(even_and_greater5, l1))
# print(l2)



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



# welsh_alphabet = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]



# You are given a list of lists of words. Given a word within the data, write a function that can predict the next following word

"""
{"I": {"am": 2}}
"""
from collections import Counter
def predict_word(data, word):
    # freq = {}

    # prev = data[0][0]
    # for j in range(len(data)):
    #     for i in range(len(data[j])):
    #         if i == 0 and j == 0: continue
    #         curr_word = data[j][i]
    #         if prev in freq:
    #             next_dict = freq[prev]
    #             if curr_word in next_dict:
    #                 next_dict[curr_word] += 1
    #             else: next_dict[curr_word] = 1
    #         else: 
    #             freq[prev] = {curr_word: 1}
    #         prev = curr_word
            
    freq = collections.defaultdict(Counter)
    for words in data:    
        for i, j in zip(words[:-1], words[1:]):
            freq[i][j] += 1
            

    # print( max(freq['I'], key = freq['I'].get, default = '') )
    # print( sorted(freq[word], key = freq[word].get)[-1] )
    #return sorted(freq[word].items(), key = lambda x: x[1], reverse=True)[0][0]


data = [
["I", "am", "Sam"],
["Green", "I", "am"],
["I", "like", "Green"],
]

# print(predict_word(data, "I"))


def remove_idxs(arr, ranges):
    max_size = len(arr)
    lookup_arr = [0] * max_size
    for range in ranges:
        start, end = range[0], range[1]
        # why not just +1 or -1
        # because we may have overlapping ranges
        # like [5,8], [5, 10]
        if start < max_size:
            lookup_arr[start] += 1
        if end < max_size:
            lookup_arr[end] -= 1

    
    sum_so_far = 0
    result = []
    for idx, num in enumerate(arr):
        sum_so_far += lookup_arr[idx]
        if sum_so_far == 0:
            result.append(num)
    return result


remove_idxs([-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76], [[5, 8], [10, 13], [3, 6], [20, 25]])



# print("".join(sorted("hia")))


#sparse search -> ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
def sparse_search(strings, target):

    def search(first, last):
        if first > last:
            return -1
        mid = (last + first) // 2
        
        if not strings[mid]:
            #adjust mid
            lo, hi = mid, mid
            while True and lo >= first and hi <= last:
                hi += 1
                lo -= 1
                if lo >= first and strings[lo]:
                    mid = lo
                    break
                if hi <= last and strings[hi]:
                    mid = hi 
                    break
            
        if target == strings[mid]:
            return mid
        elif target < strings[mid]:
            return search(first, mid - 1)
        else: return search(mid + 1, last)
    
    return search(0, len(strings) - 1)

# print(sparse_search(["dad", "", ""], "dadd"))


# Depth of a String
# find string at highest depth.

# //example 
# input: "((AB)(((CD))))"
# output: depth: 4 and string: "CD"


"""
Given a special alphabet (alien dictionary?) sort a list of words in ascedning order alphabetically:

alphabet: "a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"

Input: "ddr",  "nah", "dea", "dd", "ngah"

Output: "dea", "dd", "ddr", "ngah", "nah"
"""

welsh_alphabet = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]

#let's revise sorting by key argument
def reversed(character):
    return -ord(character)

single_word = "abuja"
print(sorted(single_word, reverse=True))
print(sorted(single_word, key=reversed))

words = ["tunde", "yemi", "yinka", "bolu"]

#infact this is what python does naturally
def reversed_word(word):
    return [-ord(c) for c in word]

print(sorted(words, reverse=True))
print(sorted(words, key=reversed_word))

#okay, back to welsh alphabet
#we can convert or cast each word to a list of numbers (based on each character) and python can sort by that

input = ["nah", "dea", " ", "dd", "ngah"]
# print("tunde"[0: 2])

welsh_dict = {word: i for i, word in enumerate(welsh_alphabet)}

#clarifying questions; how should we handle empty characters, spaces etc
def convert_to_welsh(word):
    tokens = []
    i = 0
    while i < len(word):
        if i + 1 < len(word) and word[i : i + 2] in welsh_dict:
            tokens.append(welsh_dict[word[i : i + 2]])
            i += 2
        else:
            tokens.append(welsh_dict[word[i]])
            i += 1
    
    return tokens

# print(sorted(input, key = convert_to_welsh))

# print(ord(" "))
# print(sorted(["tunde", " "]))
        
        



import math

def drawLine(x0,y0,x1,y1):
  # Imagine this is implemented. You don't need to implement
  pass
  

def drawHTree(x, y, length, depth):
    
    if depth == 0: return
    
    x0 = x - length/2
    x1 = x + length/2

    y1 = y + length/2 
    y0 = y - length/2

    #draw horizontal

    drawLine(x0, y, x1, y) # this draw the horizontal line. From (x0,y) to (xy,y) the y is the middle of H

    #draw the left verical line

    drawLine(x0, y0, x0, y1)

    #draw the right vertical line

    drawLine(x1, y0, x1, y1)
    
    # reducing (dividing) the length of the line by √2
    
    #call drawHree for the 4 endpoints
    drawHTree(x0, y1, length / math.sqrt(2), depth - 1)
    drawHTree(x0, y0, length / math.sqrt(2), depth - 1)
    drawHTree(x1, y0, length / math.sqrt(2), depth - 1)
    drawHTree(x1, y1, length / math.sqrt(2), depth - 1)
    
    #thanks a lot for the diagrams; I did not even understand the question



#https://leetcode.com/discuss/interview-question/900369/Bloomberg-or-Onsite-or-Top-K-Stocks -- assume topK can be called multiple times

#Insert, remove, get index, bisect right and left, find element inside list, are all log(n) operations. Its similar to treeset and multiset in java and c++, implemented with AVL tree or red black tree
#https://grantjenks.com/docs/sortedcontainers/sortedlist.html
from sortedcontainers import SortedDict, SortedList

class Stock:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def __lt__(self, other):
        if self.volume == other.volume:
            return self.name < other.name
        return self.volume > other.volume
        
    def __eq__(self, other):
        return self.name == other.name and self.volume == other.volume

    def __hash__(self):
        return hash((self.name, self.volume))
    

class TopKStock:
    def __init__(self):
        #I want to use SortedDict as SortedList, making all values as None lol because SortedList API is not easy to use to check if an element is present
        #You can actually use sorted list too check leader board solution below
        self.sorted_stocks = SortedDict()
        self.stock_to_curr_vol = {}
    
    
    def add_stock(self, name, volume):
      
        if name in self.stock_to_curr_vol:
            pre_vol = self.stock_to_curr_vol[name]

            old_stock = Stock(name, pre_vol)
            new_stock = Stock(name, volume)

            del self.sorted_stocks[old_stock]
            self.sorted_stocks[new_stock] = None

            del self.stock_to_curr_vol[name]
            self.stock_to_curr_vol[name] = volume

        else:
           new_stock = Stock(name, volume)
           self.sorted_stocks[new_stock] = None
           self.stock_to_curr_vol[name] = volume

    
    def getTopK(self, K):
        topK = []
        for stock in self.sorted_stocks.keys():
            topK.append((stock.name, stock.volume))
            K -= 1
            if K == 0: break

        return topK
    

topkStock = TopKStock()
topkStock.add_stock("AMZN", 50)
topkStock.add_stock("GGLE", 56)
topkStock.add_stock("AMZN", 90)
topkStock.add_stock("AMZN", 60)
topkStock.add_stock("GGLE", 96)



print(topkStock.getTopK(4))



#Hash and eq
class A:
    def __key(self):
        return (self.attr_a, self.attr_b, self.attr_c)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, A):
            return self.__key() == other.__key()
        return NotImplemented
    


from sortedcontainers import SortedList 

class Player:

    def __init__(self, playerId, score):
        self.playerId = playerId
        self.score = score

    def __lt__(self, other):
        if self.score == other.score:
            return self.playerId < other.playerId
        return self.score > other.score
        
    def __eq__(self, other):
        return self.playerId == other.playerId and self.score == other.score

    def __hash__(self):
        return hash((self.playerId, self.score))


#https://leetcode.com/problems/design-a-leaderboard/
class Leaderboard:

    def __init__(self):
        #I want to use SortedDict as SortedList, making all values as None lol because SortedList API is not easy to use to check if an element is present
        self.sorted_players = SortedList()
        self.player_to_curr_score = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.player_to_curr_score:
            
            pre_score = self.player_to_curr_score[playerId]

            old_player = Player(playerId, pre_score)
            new_player = Player(playerId, score + pre_score)

            self.sorted_players.discard(old_player)
            self.sorted_players.add(new_player)

            del self.player_to_curr_score[playerId]
            self.player_to_curr_score[playerId] = score + pre_score
            
        else:
            new_player = Player(playerId, score)
            self.sorted_players.add(new_player)
            self.player_to_curr_score[playerId] = score
            
    def top(self, K: int) -> int:
        total = 0
        for player in self.sorted_players:
            total += player.score
            K -= 1
            if K == 0: break

        return total
        

    def reset(self, playerId: int) -> None:
        pre_score = self.player_to_curr_score[playerId]
        old_player = Player(playerId, pre_score)
        self.sorted_players.discard(old_player)
        
        del self.player_to_curr_score[playerId]




# K messed 
# Your peer may be tempted to use a standard sorting algorithm such as quicksort or mergesort. However, doing so ignores the fact that the array is nearly-sorted (k-sorted) and yields suboptimal solutions.
# If your peer is stuck, ask them how the fact the array is k-sorted can help divide the array into smaller overlapping chunks (windows) and then sort them in an iterative way.
# This question is a good opportunity to check if your peer remembers Insertion Sort and Heapsort. In general, it’s an opportunity for both of you to brush up on these sorting algorithms. A good source to refresh your memory is the Sorting Algorithm Article on Wikipedia.
# Watch out for correct calculations and usage of array indices.
# If your peer can’t think of a solution, help their thought process by asking what they can do with a sliding window of size k+1.


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



def insert(data, root):
    if not root:
        return Node(data)

    if data <= root.data:
        root.left = insert(data, root.left)
    else:
        root.right = insert(data, root.right)
    
    return root

def search(data, root):
    if not root:
        return None
    if data < root.data:
        return search(data, root.left)
    elif data > root.data:
        return search(data, root.right)
    else: 
        return root

root = Node(6)
insert(7, root)
insert(4, root)
insert(3, root)
insert(19, root)
# print(root.right.right.data)

# print(search(199, root).data)


w = list('word')

w[0] = 'p'
print(w)

def collatz(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else: n = 3 * n + 1
        length += 1
    
    return length


def max_collatz_sequence(n):
    print(n)
    print()
    N = n
    maxi = 1
    memo = {}
    # c = 4
    # 3->10->5->16->8->4->2->1
    #            ^
    # memo = {16: 5, 4: 3, 1: 1}
    while n != 1:
        if n in memo:
            maxi += (memo[n] - 1)
            n = 1
            print("here")
        else:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            maxi += 1
    memo[N] = maxi

    print(memo)

    # return memo[n]


# print(collatz(3))
#print(max_collatz_sequence(2))




# print(collatz(32))

# print(5.23 == int(5.23))


class CollatzConjecture:
    def __init__(self):
        self.memo = {}
    
    def calculate_i(self, n, comb=[]):
        if n in self.memo:
            return self.memo[n]
        
        while n > 1:
            comb.append(n)
            if n % 2 == 0:
                n = n//2
            else: 
                n = 3 * n + 1
            
        comb.append(1)
        self.populateMemo(comb)
        return len(comb)

    def calculate_r(self, n):
        if n == 1:
            res = 1
        elif n % 2 == 0:
            res = 1 + self.calculate_r(n // 2) #T(n/2) + 1 if even
        else:
            res = 1 + self.calculate_r(3 * n + 1) #T(3n + 1) if odd
        
        self.memo[n] = res
        return res

    def populateMemo(self, comb):
        comb_length = len(comb)
        for i in range(comb_length):
            curr = comb[i]
            if curr not in self.memo:
                self.memo[curr] = comb_length - i



x = CollatzConjecture()
print(x.calculate_i(3))
print(x.calculate_r(3))


def collatz2(num, memo={1: 0}):
    if num in memo:
        print("here")
        return memo[num]

    if num % 2 == 0:
        res = 1 + collatz2(num//2, memo)
    else:
        res = 1 + collatz2(3*num + 1, memo)
        

    memo[num] = res
    # print(memo)
    return res


# print(collatz2(3))


