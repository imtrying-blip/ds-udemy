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
        self.array.pop(-1)
        return self.array[-1]
    
    def print_stack(self):
        return self.array
        
myStack = Stack()
# print(myStack.peek())
myStack.push('google')
print("after push google:", myStack.peek())
myStack.push('ztm')
print("after push ztm:", myStack.peek())
myStack.push('discord')
print("after push discord:", myStack.peek())
print(myStack.print_stack())
myStack.pop()
print("after pop():", myStack.peek())
# myStack.pop()
# myStack.pop()
print(myStack.print_stack())