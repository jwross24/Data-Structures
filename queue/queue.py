# from singly_linked_list.singly_linked_list import LinkedList
from stack.stack import Stack

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.
1. Implement the Queue class using an array as the underlying storage
   structure. Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?
Stretch: What if you could only use instances of your Stack class to implement
         the Queue? What would that look like? How many Stacks would you need?
         Try it!
"""


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack2.size < 1:
            if self.stack1.size < 1:  # if both stacks are empty
                return None
            else:
                # Move elements from stack 1 to stack 2 only if stack 2 is
                # empty
                while len(self.stack1) >= 1:
                    x = self.stack1.pop()
                    self.stack2.push(x)

        return self.stack2.pop()
