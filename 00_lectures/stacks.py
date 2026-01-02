# Stack Implementation: Linked Lists
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self, top=None, bottom=None, length=0):
        self.top = top
        self.bottom = bottom
        self.length = length

# peek() -> Return the top element without removing it:
    def peek(self):
        return self.top.value

# push() -> Add an element to the top of the stack:
    def push(self, value):
        new_node = Node(value)

        # Case: Adding to empty stack
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node

        else:
            holding_pointer = self.top
            self.top = new_node
            new_node.next = holding_pointer

        self.length += 1

        return self

# pop() -> Remove and return the top element:
    def pop(self):
        # Case: Empty stack
        if self.length == 0:
            return None
        
        # Case: Single node in stack
        elif self.length == 1:
            self.bottom = None

        holding_pointer = self.top
        self.top = holding_pointer.next

        self.length -= 1

        return holding_pointer
    
