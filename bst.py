from collections import deque;
class TreeNode:
    def __init__(self, data) :
        self.right = None
        self.left = None
        self.data = data
  
def insert(data, root):
    if root is None:
        root = TreeNode(data)  
    elif  data <= root.data:
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
inserttwo(7, root)
inserttwo(4, root)
inserttwo(2, root)
inserttwo(12, root)
inserttwo(22, root)
inserttwo(42, root)
inserttwo(62, root)
inserttwo(82, root)
inserttwo(99, root)
inserttwo(202, root)


# print(getHeight(root))

level_order_print(root)

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

         
        

