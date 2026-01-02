# Stack Implementation: Linked Lists
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.array = []

# peek() -> Return the top element without removing it:
    def peek(self):
        return self.array[-1]

# push() -> Add an element to the top of the stack:
    def push(self, value):
        self.array.append(value)
        return self

# pop() -> Remove and return the top element:
    def pop(self):
        last_node = self.array(-1)
        self.array.pop(last_node)
        return last_node
    
