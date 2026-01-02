# Stack Implementation: Linked Lists
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

# peek() -> Return the top element without removing it:
    def peek(self):
        return None if self.length == 0 else self.top.value

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
            # self.bottom is still the same in this case

        self.length += 1

        return self

# pop() -> Remove and return the top element:
    def pop(self):
        # Case: Empty stack
        if self.length == 0:
            return None
        
        holding_pointer = self.top

        # Case: Single node in stack
        if self.length == 1:
            self.bottom = None
            self.top == None

        else:
            self.top = holding_pointer.next

        self.length -= 1

        return holding_pointer
    
