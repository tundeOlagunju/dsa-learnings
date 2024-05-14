import collections
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.listCount = 0
        if value: 
            self.val = value
        else: self.list = []
        
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.listCount == 0

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.list.append(elem)
        self.listCount += 1

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.val = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return self.val
        return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.list if self.listCount > 0 else None


"""
nestedList - List[NestedInteger]
"""
def depthSum(nestedList):
    
    total_sum = 0
    queue = collections.deque((element, 1) for element in nestedList)

    while queue:
        curr, depth = queue.popleft()
        if curr.isInteger():
            total_sum += curr.getInteger() * depth
        else: 
            for el in curr.getList():
                queue.append((el, depth + 1))
    
    return total_sum



# build NestedInteger: [ [1,1], 2, [1,1] ]

#[1,1]
nested_1 = NestedInteger() #[]
nested_1_1 = NestedInteger(1) #1 - wrapped around an object
nested_1_2 = NestedInteger(1)  #1

nested_1.add(nested_1_1)
nested_1.add(nested_1_2)

#2
nested_2 = NestedInteger(2)


#[1,1]
nested_3 = NestedInteger()
nested_3_1 = NestedInteger(1)
nested_3_2 = NestedInteger(1)

nested_3.add(nested_3_1)
nested_3.add(nested_3_2)

print(depthSum([nested_1, nested_2, nested_3]))




#build [ [ [ 1 ] ] ]

nested4_inner_most = NestedInteger()

nested4_mid = NestedInteger()

nested4_outer_most = NestedInteger(1)  #1
nested4_mid.add(nested4_outer_most) # [ 1 ]
nested4_inner_most.add(nested4_mid) # [ [ 1 ] ]

print(depthSum([ nested4_inner_most ]))  # [ [ [ 1 ] ] ]