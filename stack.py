#stack is implemented with linked list that just exposes two major functions push and pop as well as peek and isEmpty
#can also be implemented with a dynamic array
# The main advantage of using LinkedList over array for 
#is that array has fixed size in memory and needs to be resized which makes some append operations take longer
#use deque implementation instead in python

#undo feature is implemented with stack

#similarly for queue

#custom implementation of a class called Stack for Stack of Plates problem in CTCI

class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        
