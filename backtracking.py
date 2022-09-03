
def generateParenthesis(n):

    res = []
    def build_combination(open_count, close_count, curr_comb):
        if len(curr_comb) == 2 * n:
            print(n)
            res.append("".join(curr_comb))
            return
        
        if open_count < n:
            print("here")
            curr_comb.append("(")
            build_combination(open_count+1, close_count, curr_comb)
            curr_comb.pop()
        
        if close_count < open_count:
            curr_comb.append(")")
            build_combination(open_count, close_count+1, curr_comb)
            curr_comb.pop()
        
    
    build_combination(0, 0, [])
    return res

# print(generateParenthesis(2))



def permuteUnique(nums):
    result = []
    done = set()
    def permute(perms, used):
        if len(perms) == len(nums):
            result.append(perms[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in perms:       
                perms.append(nums[i])
                permute(perms, used)
                # used[i] = False
                perms.pop()

    
    permute([], [False]*len(nums))
    return result

def permute(nums):
    result = []
    def permute(perms):
        if len(perms) == len(nums):
            result.append(perms[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in perms:       
                perms.append(nums[i])
                permute(perms)
                perms.pop()

    
    permute([])
    return result
res = permute([1,2,3])
# res = permuteUnique([1,2,3])
# s = set(tuple(x) for x in res)
print(res)


# def subsets(nums):
#     res = []

#     def build_subset(path, curr_index):
#         res.append(path[:])
#         for i in range(curr_index, len(nums)):   
#             path.append(nums[i])
#             build_subset(path, i+1)
#             path.pop()
            
#     build_subset([], 0)
#     return res

# # print(subsets([1,2,3]))

# def subsets_dups(nums):
#     res = []
#     nums.sort()

#     def build_subset(path, curr_index, used):
#         res.append(path[:])
#         for i in range(curr_index, len(nums)):
#             if i > 0 and nums[i] == nums[i-1] and not used[i-1]: 
#                 continue 
#             used[i] = True  
#             path.append(nums[i])
#             build_subset(path, i+1, used)
#             path.pop()
#             used[i] = False
            
#     build_subset([], 0, [False]*len(nums))
#     return res

# print(subsets_dups([1,2,2]))


def subsets_dups(nums):
    res = []
    nums.sort()

    def build_subset(path, curr_index):
        res.append(path[:])
        for i in range(curr_index, len(nums)):
            if i > curr_index and nums[i] == nums[i-1]: 
                continue 
            path.append(nums[i])
            build_subset(path, i+1)
            path.pop()
            
    build_subset([], 0)
    return res

print(subsets_dups([1,2,2]))


def combinationSum(nums, target):
    res = []
    nums.sort()
    def build_combination(curr_comb, start):
        if sum(curr_comb) == target:
            res.append(curr_comb[:])
            return
        
        if sum(curr_comb) > target:
            return

        for i in range(start, len(nums)):
            # if curr_comb and nums[i] < curr_comb[-1]: continue
            curr_comb.append(nums[i])
            build_combination(curr_comb, i) #i and not start please (you keep making this mistake) and with this you will not need the if condition in the for loop, but with start you will need it
            curr_comb.pop()

    build_combination([], 0 )
    return res

# print(combinationSum([2,3,6,7], 7))


def combinationSum2(nums, target):
    res = []
    nums.sort()
    def build_combination(curr_comb, start, remain):
        if remain < 0: 
            return
        elif remain == 0:
            res.append(curr_comb[:]) 
            return
        for i in range(start, len(nums)):
            # if nums[i] > remain:
            #     continue
            curr_comb.append(nums[i])
            build_combination(curr_comb, i, remain - nums[i]) #i because we can reuse element, not start please
            curr_comb.pop()

    build_combination([], 0 , target)
    return res

# print(combinationSum2([2,3,6,7], 7))



def combinationSumDups(nums, target):
    res = []
    nums.sort()
    def build_combination(curr_comb, start):
        if sum(curr_comb) == target:
            res.append(curr_comb[:])
            return
        
        if sum(curr_comb) > target:
            return

        for i in range(start, len(nums)):
            #we need to avoid duplicates, some people keep used variable as well
            if i > start and nums[i] == nums[i-1]:
                continue
            curr_comb.append(nums[i])
            build_combination(curr_comb, i+1) #i+1 we cannot reuse number
            curr_comb.pop()

    build_combination([], 0 )
    return res

print(combinationSumDups([10,1,2,7,6,1,5], 8))


def partition(string):
    res = []
    def isPalindrome(s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

    def build_partition(curr_comb, start):
        if start == len(string):
            res.append(curr_comb[:])
            return
        
        for i in range(start, len(string)):
            if isPalindrome(string, start, i):
                curr_comb.append(string[start: i+1])
                build_partition(curr_comb, i+1)
                curr_comb.pop()

    build_partition([], 0)
    return res


print(partition("aabb"))




