# def factorial(number):
#     if number == 0 or number == 1:
#         return 1
#     return number * factorial(number - 1)

# print(factorial(5))

# def recursive_sum(list):
#     if not list:
#         return 0
#     return list[0] + recursive_sum(list[1:])

string = "tunde"
print(string[0:1])

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


def func(l):
    # l.append(1)

    l = l + [1]
    print(l)
    if len(l) < 10:
        func(l)
        print("returning...", len(l))
    return l

l = []
print(func(l))
# print(l)