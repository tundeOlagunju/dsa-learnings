from collections import deque;
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
print(root.left.data)

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
