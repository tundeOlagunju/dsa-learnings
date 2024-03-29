
def countNode(head):
    count = 1
    current = head
    while current.next:
        count += 1
        current = current.next
    return count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    

    def insertNodeAtBeginning(self, data):
        new_node = Node(data)
        # if not self.head: 
        #     self.head = new_node
        #     return
        new_node.next = self.head
        self.head = new_node
    
    def removeTopNode(self):
        if not self.head:
            print('No node to remove')
            return
        self.head = self.head.next
        
    
    def insertNodeAtNthPosition(self, data, n):
        if n > self.getSize():
            print('Insert position is not valid')
            return 
        if n == 0 or not self.head: 
            self.insertNodeAtBeginning(data)
            return

        new_node = Node(data)
        current_node = self.head
        for i in range(n-1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
    
    def deleteAtNthPosition(self, n):
        if n >= self.getSize():
            print('Delete position is not valid')
            return 

        if n == 0: 
            self.head = self.head.next
            return
        
        current_node = self.head
    
        for i in range(n-1):
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next
    
    def findData(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                print('Found:', data)
                return data
            current_node = current_node.next

        print('Not Found:', data)
        
    
    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def getSize(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        
        # print('Current size of linkedList is', size)
        return size

    def reverse(self):
        curr = self.head
        newHead = None
        while curr:
            next = curr.next #note; next is a built-in function in python avoid assigning to it
            curr.next = newHead 
            newHead = curr
            curr = next
        self.head = newHead

    def reverseLinkedList(self):
        prev, curr = None, self.head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            
    def reverseRecursive(self):
        def reverse(head, newHead):
            if not head:
               return newHead
            next = head.next
            head.next = newHead 
            return reverse(next, head)

        self.head = reverse(self.head, None)

    def kthToLast(self, k):
        self.lent = 0
        def kthToTheLast(head, counter):
            if head is None:
                self.lent = counter
                return None
            node = kthToTheLast(head.next, counter + 1)
            if k == self.lent - counter - 1:
                return head
            return node
        return kthToTheLast(self.head, 0)


    
           
def swapFirstTwoPairs(head):
    # def swap(head):  
    #     if not head or not head.next:
    #         return head
    #     temp = head
    #     temp_2 = head.next.next
    #     head = head.next
    #     head.next = temp
    #     temp.next = temp_2
    #     return swap(head.next.next)
   
    if not head or not head.next:
        return head

    temp = head
    temp_2 = head.next.next
    head = head.next
    head.next = temp
    temp.next = temp_2
    
    
    swapFirstTwoPairs(temp_2)
    return head
        
        # if not self.head or not self.head.next:
        #     return
        # self.head ,self.head.next = self.head.next ,self.head
        # self.head.next

# soft   
def sumLists(head1, head2, carry):
    if not head1 and not head2:
        return None
    if not head1:
        return Node(head2.data + carry)
    if not head2:
        return Node(head1.data + carry)
    else:
        new_node = Node((head1.data + head2.data) % 10 + carry)
        new_node.next = sumLists(head1.next, head2.next, (head1.data + head2.data) // 10)
        return new_node


def isListPalindrome(head):
    pass


linked_list = LinkedList()
# linked_list.getSize()
# linked_list.deleteAtNthPosition(0)
# linked_list.insertNodeAtNthPosition(12, 1)
linked_list.insert(7)
# linked_list.insert(1)
linked_list.insert(1)
linked_list.insert(6)
# linked_list.insert(3)
# linked_list.insert(4)
# linked_list.insert(5)



linked_list2 = LinkedList()
# linked_list.getSize()
# linked_list.deleteAtNthPosition(0)
# linked_list.insertNodeAtNthPosition(12, 1)
linked_list2.insert(5)
# linked_list.insert(1)
linked_list2.insert(9)
linked_list2.insert(2)
# linked_list2.insert(3)
# linked_list2.insert(4)
# linked_list2.insert(5)
# linked_list.reverse()
# linked_list.reverseRecursive()
# print(swapFirstTwoPairs(linked_list.head))
# linked_list.insertNodeAtNthPosition(12, 1)
# linked_list.removeTopNode()

# linked_list.insert(8)
# linked_list.insertNodeAtBeginning(4)
# linked_list.insertNodeAtBeginning(9)
# linked_list.insert(0)
# linked_list.insertNodeAtNthPosition(12, 2)
# linked_list.insertNodeAtNthPosition(13, 5)
# linked_list.insertNodeAtNthPosition(11, 0)
# linked_list.deleteAtNthPosition(0)
# linked_list.deleteAtNthPosition(2)
# linked_list.deleteAtNthPosition(0)
# linked_list.deleteAtNthPosition(3)
# linked_list.findData(444)

# linked_list.printLinkedList()
# print('Size of LinkedList is', linked_list.getSize())

# print(linked_list.kthToLast(0).data)

res = sumLists(linked_list.head, linked_list2.head, 0)
while res:
    print(res.data)
    res = res.next


# head  = Node(5)
# nodeB = Node(5)
# nodeC = Node(5)
# nodeD = Node(5)

# head.next = nodeB
# nodeB.next = nodeC
# nodeC.next = nodeD

# print(countNode(head))

