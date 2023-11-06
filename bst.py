#https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python --> tree visualizer

from collections import deque
import collections;
class TreeNode:
    def __init__(self, data) :
        self.right = None
        self.left = None
        self.data = data
  
def insert(data, root):
    if root is None:
        root = TreeNode(data)  
    elif data <= root.data:
        root.left = insert(data, root.left)
    else:
        root.right = insert(data, root.right)
    return root

def inserttwo(data, root):
    if root is None:
        root = TreeNode(data)
        return 
    if data <= root .data:
        if root.left is None:
            root.left = TreeNode(data) 
        else: inserttwo(data, root.left)
    else:
        if root.right is None:
            root.right = TreeNode(data)
        else: inserttwo(data, root.right)

def search(data, root):
    if not root:
        return -1
    if data == root.data:
        return data
    elif data < root.data:
        return search(data, root.left)
    else: 
        return search(data, root.right)

def getMin(root):
    if root is None:
        return -1
    while root.left:
        root = root.left
    return root.data 

def getMax(root):
    if root is None:
        return -1
    while root.right:
        root = root.right
    return root.data 

def getMinRec(root):
    if root is None:
        return -1
    if root.left is None:
        return root.data
    return getMinRec(root.left)

def getMaxRec(root):
    if root is None:
        return -1
    if root.right is None:
        return root.data
    return getMaxRec(root.right)
    
def getHeight(root):
    if root is None:
        return -1
    return max ( getHeight(root.left), getHeight(root.right) ) + 1

def isBinarySearchTree(root):
    # TODO
    pass

def isSubTreeLesser(root, value):
    pass
    
def isSubTreeGreater(root):
    pass 

def deleteNode(root):
    # TODO
    pass

def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print(root.data)
    in_order_print(root.right)

def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.left)
    pre_order_print(root.right)

def level_order_print(root):
    if not root:
        return
    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()
        if current.left : queue.append(current.left)
        if current.right: queue.append(current.right)
        print(current.data)
    

# r = TreeNode(3)
# insert(7, r)
# insert(1, r)
# insert(5, r)

# in_order_print(r)


root = TreeNode(6)
insert(7, root)
insert(4, root)
# print(root.left.data)

inserttwo(2, root)
inserttwo(12, root)
inserttwo(22, root)
inserttwo(42, root)
inserttwo(62, root)
inserttwo(82, root)
inserttwo(99, root)
inserttwo(202, root)
# print(search(2, root))


# print(getHeight(root))

# level_order_print(root)

# print(search(7, root))
# print(search(6, root))
# print(search(4, root))
# print(search(2, root))
# print(search(12, root))
# print(search(0, root)) #not found

# print(getMin(root))
# print(getMax(root))

# print(getMinRec(root))
# print(getMaxRec(root))

# pre_order_print(root)

         
ch =  {"a": 1, "b": 2, "c": 3}
# print(list(ch.keys()))   

#To construct a bst from a preorder array of elements e.g [2,1,3], one could take each element in the array and call insert() 
# to insert each. each insertion takes O(logN) in avg case and therefore this takes NlogN in total
# There is a better approach to insert these elements in O(N) time 

    # i = 0
    # def bstFromPreorder(self, A, bound=float('inf')):
    #     if self.i == len(A) or A[self.i] > bound:
    #         return None
    #     root = TreeNode(A[self.i])
    #     self.i += 1
    #     root.left = self.bstFromPreorder(A, root.val)
    #     root.right = self.bstFromPreorder(A, bound)
    #     return root


    #or without maintaining i
    
    # def bstFromPreorder(self, A):
    #     return self.buildTree(A[::-1], float('inf'))

    # def buildTree(self, A, bound):
    #     if not A or A[-1] > bound: return None
    #     node = TreeNode(A.pop())
    #     node.left = self.buildTree(A, node.val)
    #     node.right = self.buildTree(A, bound)
    #     return node



    # bst from post order  https://leetcode.com/problems/serialize-and-deserialize-bst/solution/ data is a list

        # def deserialize(self, data):
        # """
        # Decodes your encoded data to tree.
        # """
        # def helper(lower = float('-inf'), upper = float('inf')):
        #     if not data or data[-1] < lower or data[-1] > upper:
        #         return None
            #   data = [1,3,2] for example
        #     val = data.pop()
        #     root = TreeNode(val)
        #     root.right = helper(val, upper)
        #     root.left = helper(lower, val)
        #     return root


# bst from preorder https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93171/Python-O(-N-)-solution.-easy-to-understand vals is a deque tobe able to pop from left in const time
    # # O( N ) since each val run build once
    # def deserialize(self, data):
    #     vals = collections.deque(int(val) for val in data.split())

    #     def build(minVal, maxVal):
    #         if vals and minVal < vals[0] < maxVal:
    #             val = vals.popleft()
    #             node = TreeNode(val)
    #             node.left = build(minVal, val)
    #             node.right = build(val, maxVal)
    #             return node

    #     return build(float('-infinity'), float('infinity'))




    
def buildTreeWithMinimalHeight(sortedArray, l, r):
    if l > r:
        return
    mid = (l + r ) // 2
    root = TreeNode(sortedArray[mid])
    root.left = buildTreeWithMinimalHeight(sortedArray, l, mid - 1)
    root.right = buildTreeWithMinimalHeight(sortedArray, mid + 1, r)
    return root


res = buildTreeWithMinimalHeight([1,2,3,4], 0, 3)
# level_order_print(res)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def listOfDepths(root):

    queue = collections.deque([root])
    res = []
    while queue:
        head = Node()
        currNode = head
        for _ in range(len(queue)):
            curr = queue.popleft()

            currNode.next = Node(curr.data)
            currNode = currNode.next

            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        
        res.append(head.next)
    
    return res


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph) - 1
        results = []

        def backtrack(curr_node, path):
            # if we reach the target, no need to explore further.
            if curr_node == target:
                results.append(list(path))
                return
            # explore the neighbor nodes one after another.
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()
        # kick of the backtracking, starting from the source node (0).
        path = [0]
        backtrack(0, path)

        return results      
    


   
def weaveList(left, right, prefix, result):
    if not left or not right:
        res = prefix[:]
        res.extend(left)
        res.extend(right)
        result.append(res)
        return
    
    prefix.append(left.pop(0))
    weaveList(left, right, prefix, result)
    left.append(prefix.pop())

    prefix.append(right.pop(0))
    weaveList(left, right, prefix, result)
    right.append(prefix.pop())

def allSequences(start):
    if not start:
        return [[]]
    
    left_seq = allSequences(start.left)
    right_seq = allSequences(start.right)
    # print(left_seq, right_seq)

    result = []
    for left in left_seq:
        for right in right_seq:
            weaved = []
            weaveList(left, right, [start.data], weaved)
            result.extend(weaved)   
    return result


root2 = TreeNode(6)
insert(7, root2)
insert(4, root2)

bst_sequences = allSequences(root2)
# print(bst_sequences)


# For every non-root node in a binary tree, return the new height of the binary tree if the subtree rooted at that node were deleted.You are given a pointer to the root of the tree, you need to return a list of pair of integers {X, F(X)} for every node X in the given tree. Here, F(X) represents the updated height of the original tree if the subtree rooted at node X is deleted.

# The order of the elements in the result list doesn't matter.
# In the following example, X = 5 i.e. subtree rooted at node 5 is deleted.

	# 	  1                 1
	#    /\\               /\\
	#   2   3   ===>      2  3
	#      /\\              /
	# 	4    5            4
	# 		 \\
	# 		  6

    # The goal is to compute this for all non-root nodes and thus arrive at: [{2, 3}, {3, 1}, {4, 3}, {5, 2}, {6, 2}].


def binaryTreeAfterDeletion(tree_root):

    height_map = collections.defaultdict(int)
    result = []

    def computeNodeHeight(start):
        if not start:
            return 0
        
        left_height = computeNodeHeight(start.left)
        right_height = computeNodeHeight(start.right)
        height = max(left_height, right_height) + 1
        height_map[start] = height
        return height
    
    def computeNodeHeightAfterDeletion(start, level, max_height_so_far):
        if not start:
            return

        if level > 0:
            result.append((start.data, max_height_so_far))
        
      
        computeNodeHeightAfterDeletion(start.left, level + 1, max(max_height_so_far, height_map[start.right] + level))
        computeNodeHeightAfterDeletion(start.right, level + 1, max(max_height_so_far, height_map[start.left] + level))

    computeNodeHeight(tree_root)
    computeNodeHeightAfterDeletion(tree_root, 0, 0)
    return result



root4 = TreeNode(6)
insert(7, root4)
insert(9, root4)
insert(4, root4)
print(binaryTreeAfterDeletion(root4))


        