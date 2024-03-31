# def factorial(number):
#     if number == 0 or number == 1:
#         return 1
#     return number * factorial(number - 1)

# print(factorial(5))

# def recursive_sum(list):
#     if not list:
#         return 0
#     return list[0] + recursive_sum(list[1:])

# string = "tunde"
# print(string[0:1])

# print(recursive_sum([1,2,5]))


# def count_items_in_list(list):
#     if not list:
#         return 0
#     return 1 + count_items_in_list(list[1:])

# print(count_items_in_list([1,2,3,4,4,5]))


# def max_in_list(list):
#     if not list:
#         return 0
#     return max(list[0], max_in_list(list[1:]))

# print(max_in_list([9,1,2,123,3,0,7]))
# print(max_in_list([1]))


#     # hi = len(list) - 1
#     # low = 0

#     # while hi >= low:
#     #     mid = (hi + low)//2
#     #     guess = list[mid]
#     #     if guess == item:
#     #         return guess
#     #     elif guess > item:
#     #         hi = mid - 1
#     #     else: low = mid + 1
    
#     # return None

# def binary_search_recursive(list, item, hi=None, lo=0):
#     if hi is None:
#         hi = len(list) - 1
#     #base case 
#     if hi <= lo:
#         return list[lo] if item == list[lo] else None
#     mid = (hi + lo)//2
#     if (list[mid] > item):
#         return binary_search_recursive(list, item, mid - 1, lo)
#     elif list[mid] == item: return item
#     else: return binary_search_recursive(list, item, hi, mid + 1)


# print(binary_search_recursive([1, 2, 3, 4, 5], 11))
# print(binary_search_recursive([1, 2, 3, 4, 5], -1))
# print(binary_search_recursive([1, 2, 3, 4, 5], 5))


# list = [[i for i in range(x)] for x in range(4)]

# list2 = [[1, 2] , [3, 4]]

# for j in range(2):
#     for i in range(2):
#         print( list2[i][j] )
 
# def longestCommonPrefix(strs) -> str:
#     l = zip(*strs)
#     # print(list(l))
#     prefix = ""
#     for i in l:
#         print(set(i))
#         if len(set(i))==1:
#             print('here')
#             prefix += i[0]
#         else:
#             break
#     return prefix

# print(longestCommonPrefix(["flower","flow","flight"]))


# def func(l):
#     # l.append(1)

#     l = l + [1]
#     print(l)
#     if len(l) < 10:
#         func(l)
#         print("returning...", len(l))
#     return l

# l = []
# print(func(l))
# print(l)


def compute_tower_of_hanoi(num_rings):

    def compute(num_rings, from_tower, to_tower, use_tower):
        if num_rings <= 0:
            return
        
        #move n - 1 rings from from_tower to use_tower using to_tower
        compute(num_rings - 1, from_tower, use_tower, to_tower)
        to_move = pegs[from_tower].pop()
        pegs[to_tower].append(to_move)
        print(f"Move {to_move} from {from_tower} to {to_tower}.") 
        compute(num_rings - 1, use_tower, to_tower, from_tower)

    
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, 3)]
    compute(num_rings, 0, 1, 2)


# compute_tower_of_hanoi(3)


# def sum_up_to_n(n):
#     if n == 0:
#         return 0
#     return n + sum_up_to_n(n-1)

# print(sum_up_to_n(4))

#Write a function that counts the number of ways you can partition n objects using parts up to m (m >= 0) 
#n = 5, m = 3 no of partitions = 5

# def count_number_of_partitions(n, m):
#     if m == 0 or n < 0: return 0
#     if n == 0: return 1
#     # if n < m : return count_number_of_partitions(n, n) 
#     return count_number_of_partitions(n, m - 1) + count_number_of_partitions(n - m, m)


# print(count_number_of_partitions(5, 3))   


def deleteMiddle(stack):

    def delete(k):
        if len(stack) == k: 
            stack.pop()
            return stack
        
        temp = stack.pop()
       
        delete(k)
        stack.append(temp)
        return stack
    
    
    return delete(len(stack) // 2 + 1)

print(deleteMiddle([1,2,4,5]))


#Whats the Time complexity of this algo. 
#We know TC of computing n fib is 2^N (2T(N-1) + 1), shouldnt this be N * 2 ^ N ??? Nooo
# fib(1) -> 2 ^ 1 = 1
# fib(2) -> 2 ^ 2 = 4
# fib(3) -> 2 ^ 3 = 8
# fib(N) -> 2 ^ N
#Therefore total TC is 2 ^ 0 + 2 ^ 1 + 2 ^ 2 + ... 2 ^ N =  2 ^ N + 1 - 1 = 2 ^ N
def allFib(n):

    def fib(n): 
        if n <= 0 : return 0
        elif n ==  1: return 1
        return fib(n - 1) + fib(n - 2)

    for i in range(n):
        print(fib(i))


#Time complexity of cached version = O(N)
def fibonacci(n):

    memo = [0 for _ in range(n)]

    def fib(i):
        if i == 0 or i == 0: return i

        if memo[i] == 0:
            memo[i] = fib(i - 1) + fib(i - 2)
        
        return memo[i]
    
    return fib(n)

memo = {}
def fib(N):

	if N == 0: return 0
	if N == 1: return 1

	if N-1 not in memo: memo[N-1] = fib(N-1)
	if N-2 not in memo: memo[N-2] = fib(N-2)

	return memo[N-1] + memo[N-2]

from functools import lru_cache
from re import I
class Solution:
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n < 2: return n
        return self.fib(n-1) + self.fib(n-2)




#whats the Tc of this? dont be confused and jump to kO(2^K) i.e K (2 T(K - 1) + 1) recurrence function because we call getNum k times. where k is the rowIndex. This is wrong. 
# 1. getNum(k, 0) -> 2 ^ 0
# 2. getNum(k, 1) -> 2 ^ 1
# 2. getNum(k, 2) -> 2 ^ 2
# summing this up: 2 ^ 0 + 2 ^ 1 + 2 ^ 2 + ... + 2 ^ k = 2 ^ K + 1. - 1 = 2 ^ k (Power series)
# Therefore TC is still 2 ^ K
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
        
#         def getNum(row, col):
#             if not row or not col or row == col:
#                 return 1
            
#             return getNum(row - 1, col - 1) + getNum(row - 1, col)
        
        
#         return [getNum(rowIndex, i) for i in range(rowIndex + 1)]
    

#Fibonacci memoized TC -> O(K^2) . It takes O(K) to calculate the fibonacci of k where k is rowIndex and we do that k times 
# 1 -> 1
# 2 -> 2
# 3 -> 3 etc

# 1 + 2 + 3 + 4 + ... K = K (K+1) / 2 = O(K^2)
def getRow(rowIndex):

    memo = {}

    def helper(rowIndex, colIndex):
        if not rowIndex or not colIndex or rowIndex == colIndex:
            return 1
        
        if (rowIndex, colIndex) in memo:
            return memo[(rowIndex, colIndex)]

        memo[(rowIndex, colIndex)] =  helper(rowIndex - 1, colIndex - 1) + helper(rowIndex - 1, colIndex)
        return memo[(rowIndex, colIndex)]

    return [helper(rowIndex, i) for i in range(rowIndex + 1)]




#Robot in a Grid. CTCI 8.2. Variation of unique paths on LC
#This question is basically DFS (but starting from the target (bottom right) to (top left)) in reverse direction

def getPath(maze):

    def dfs(row, col):
        if row < 0 or row > len(maze) - 1 or col < 0 or col > len(maze[0]) - 1:
            return False
        
        if (row, col) in failed_paths:
            return False

        #if I am at origin
        if row == 0 and col == 0:
            path.append((row, col))
            return True
        
        #if there's a path from start to here, add my location
        if dfs(row, col - 1):
            path.append((row, col))
            return True

        #if there's a path from start to here, add my location
        if dfs(row - 1, col):
            path.append((row, col))
            return True
        
        failed_paths.add((row, col))
     
        return False
        

    if not maze: return 
    path = []
    failed_paths = set()
    dfs(len(maze) - 1, len(maze[0]) - 1)
    # print(failed_paths)
    return path


maze = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# print(getPath(maze))







#Leetcode solution
def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    #If we found a way to create the desired amount
    if amount == 0: 
        return 1 
    
    #If we went over our amount or we have no more coins left
    if amount < 0 or len(coins) == 0:
        return 0 

    #Our solutions can be divided into two sets,
    #   1) Solutions that cointain the coin at the end of the coins array 
    #   2) Solutions that don't contain that coin 
    return change(amount - coins[-1], coins) + change(amount, coins[:-1]) 

#Neetcode
def change2(amount, coins):

    def dfs(i, a):
        if a == amount:
            return 1
        if a > amount:
            return 0
        if i == len(coins):
            return 0
        way1 = dfs(i, a + coins[i])
        way2 = dfs(i + 1, a)
        return way1 + way2
    
    return dfs(0, 0)

def change5(amount, coins):
    res = []
    def dfs(i, a, comb):
        if a == amount:
            res.append(list(comb))
            return 1
        if a > amount:
     
            return 0
        if i == len(coins):
        
            return 0
        
        comb.append(coins[i])
        way1 = dfs(i, a + coins[i], comb)
        
        comb.pop()
        way2 = dfs(i + 1, a, comb)
        #comb.pop()
        return way1 + way2
    
    dfs(0, 0, [])
    return res


#this is unmemoizable -> this solution sort of feels like backtracking, this is not theb right way to think about this problem, although it works (TLE on leetcode)
#we should think in a way that, can we solve bigger problems by solving the sub problems?? 
def change3(amount, coins):
   
    def dfs2(amount, currentIndex):
        if amount == 0:
            return 1
        if amount < 0:
            return 0

        ways = 0
        for i in range(currentIndex, len(coins)):
            print(amount - coins[i])
            ways += dfs2(amount - coins[i], i)

        #memo[(amount, currentIndex)] = ways
        return ways
    
    return dfs2(amount, 0)
    


#CTCI solution
def coins(money, coins):

    def makeChange(coins, money, index):
        if money == 0:
            return 1
        if index >= len(coins):
            return 0
        amountWithCoin = 0
        ways = 0
        while amountWithCoin <= money:
            remaining = money - amountWithCoin
            ways += makeChange(coins, remaining, index + 1)
            amountWithCoin += coins[index]
        
        return ways
    
    return makeChange(coins, money, 0)


# print(change(6, [1, 5, 10, 25]))

# print(coins(6, [1, 5, 10, 25]))

print(change5(4, [1, 2]))


# Find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

# Input: 2
# Output: ["aa", "ab", "ba", "bb"]

# Input: 4
# Output: ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"]


def n_letter_words(n):
    
    result = []

    def compute(comb = []):
        if len(comb) == n:
            result.append("".join(comb[:]))
            return
        
        for char in ["a", "b"]:
            comb.append(char)
            compute(comb)
            comb.pop()

    compute()
    return result


print(n_letter_words(4))

