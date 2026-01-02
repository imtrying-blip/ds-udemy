class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next # Pointer to the next NODE in the list, default is None
        # If next is None, this node is currently the tail

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1


    # Create an append method for the LinkedList class
    # Goal:
    # Add a new value to the end of the linked list in O(1) time.

    # Before appending, the list looks like:
    #     head → ... → tail → None
    # After appending:
    #     head → ... → old_tail → new_node → None
    def append(self, value):
        new_node = Node(value)
            # Creates a new node that stores value
            # new_node.next is automatically None
            # This node is not connected to the list yet
        self.tail.next = new_node 
            # self.tail is the current last node
            # We point the old tail to the new node (link to the new node) -> the key pointer update
            # the chain now includes the new node
        self.tail = new_node
            # Update the tail to be the new node
            # Why this matters:
                # Without this, future appends would still think the old tail is last
                # Keeping a tail pointer is what makes append O(1)
        self.length += 1
            # Increment the length of the list to reflect the new node added
        return self
# Why append is O(1)
# Because we store self.tail, we:
    # Do not traverse the list
    # Update exactly two pointers
# SUMMARY:
# append creates a new node, links it to the current tail, updates the tail reference, and increments the list length — adding an element to the end in constant time.


    # Create a prepend method for the LinkedList class
    # Goal:
    # Add a new value to the start of the linked list in O(1) time.
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
            # Point the new node's next to the current head -> key pointer update
        self.head = new_node
        self.length += 1
    # or    
    def prepend_v2(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.length += 1
        return self
    
    def insert(self, index, value):
        # Check params
        if index >= self.length:
            return self.append(value)
            # If the index to insert is greater than or equal to the length, append to the end
        if index == 0:
            return self.prepend(value)
            # If the index is 0, prepend to the start

        new_node = Node(value)
        insert_after_this_node = self.traverse_to_node(index - 1)
        insert_before_this_node = insert_after_this_node.next #holding_pointer
        insert_after_this_node.next = new_node
        new_node.next = insert_before_this_node

        self.length += 1
        return self
    
    def traverse_to_node(self, index):
        current_index = 0
        current_node = self.head
        while current_index != index:
            current_node = current_node.next
            current_index += 1
        return current_node
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        
        # Edge case: remove head
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            # Update tail if list is now empty
            if self.length == 0:
                self.tail = None

            return self
        
        leader = self.traverse_to_node(index - 1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next

        # Update tail if the deleted node was the old tail
        if unwanted_node == self.tail:
            self.tail = leader

        self.length -= 1
        return self

    def reverse(self):
            current = self.head
            previous = None

            while current:
                temp = current.next
                current.next = previous #reverse pointer
                previous = current
                current = temp
            
            # Assign new head and tail
            self.head = previous
            self.tail = current
                # NOTE: current is None at loop end

            return self
    
# NC 206. Reverse Linked List   
    # Given the beginning of a singly linked list head, reverse the list, and return the new head of the list
    
    def reverse_list(self):
        cur = self.head
        prev = None
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

    # To visualise the LinkedList as an array:
    def print_list(self):
        list = []
        current_node = self.head
        while current_node is not None:
            list.append(current_node.value)
            current_node = current_node.next
        return list
    
myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16) 
myLinkedList.prepend(1)
myLinkedList.insert(2, 99) #[1, 10, 99, 5, 16]
myLinkedList.insert(20, 88) #[1, 10, 99, 5, 16, 88]
myLinkedList.remove(2) #[1, 10, 5, 16, 88]
print(myLinkedList.print_list()) 
myLinkedList.reverse()
myLinkedList.reverse_list()
print("Reversed list:", myLinkedList.print_list()) 
