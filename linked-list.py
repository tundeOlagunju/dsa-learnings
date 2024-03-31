
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



class LinkedList2:
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
    
    def insertNodeAtBeginning(self, data, cloned):
        new_node = Node(data)
        new_node.next = cloned.head
        cloned.head = new_node
        return cloned
    
    def reverse(self):
        cloned = LinkedList2()
        while self.head:
            cloned = self.insertNodeAtBeginning(self.head.data, cloned)
            self.head = self.head.next
        return cloned
    
    def as_list(self):

        as_list = []
        while self.head:
            as_list.append(self.head.data)
            self.head = self.head.next
        
        return as_list


ll2 = LinkedList2()
ll2.insert(3)
ll2.insert(4)
ll2.insert(5)

print(ll2.reverse().as_list())
# print(ll2.as_list())


def complete_inventory(whx, x, why, y):
    placement_index = len(whx) - 1
    whx_pointer = x - 1
    why_pointer = y - 1

    while whx_pointer >= 0 and why_pointer >= 0:
        if whx[whx_pointer] > why[why_pointer]:
            whx[placement_index] = whx[whx_pointer]
            whx_pointer -= 1
        else:
            whx[placement_index] = why[why_pointer]
            why_pointer -= 1
        placement_index -= 1

    while whx_pointer >= 0:
        whx[placement_index] = whx[whx_pointer]
        whx_pointer -= 1
        placement_index -= 1
    
    while why_pointer >= 0:
        whx[placement_index] = why[why_pointer]
        why_pointer -= 1
        placement_index -= 1
    
    return whx


print(complete_inventory([2,3,4,0,0,0], 3, [1,5,9], 3))



def findSpy(num_people, has_information) -> int:
    if num_people <= 0: return -1

    spy = -1

    in_degree = [0] * num_people
    out_degree = [0] * num_people
    
    for person1, person2 in has_information:
        in_degree[person2 - 1] += 1
        out_degree[person1 - 1] += 1
    
    print(in_degree, out_degree)
    for i, degree in enumerate(out_degree):
        if degree == num_people - 1:
            spy = i + 1
            break
    
    if spy == -1:
        return 0
    
    return spy if in_degree[spy - 1] == 0 else 0


print(findSpy(2, [[1,2]]))

print([[0 for _ in range(3)] for _ in range(3)])