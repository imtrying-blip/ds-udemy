class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next # Pointer to the next NODE in the list, default is None
            # If next is None, this node is currently the tail
        self.previous = previous # Pointer to the previous NODE in the list, default is None


class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
        print("length at intialisation", self.length)

# Create an append method to ADD a new value to the END of the linked list in O(1) time
    # Before appending, the list looks like:
    #     head → ... → tail → None
    # After appending:
    #     head → ... → old_tail → new_node → None
    def append(self, value):
        new_node = Node(value)
            # Creates a new node that stores value
            # new_node.next is automatically None
            # This node is not connected to the list yet

        new_node.previous = self.tail
            # assign before updating pointers

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
        print(self.length)
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
        # self.head.previous = new_node
        
        new_node.next = self.head
            # Point the new node's next to the current head -> key pointer update
        new_node.previous = new_node
        self.head = new_node
        self.length += 1
        print(self.length)
        return self
    # or    
    def prepend_v2(self, value):
        new_node = Node(value, self.head)
        new_node.previous = new_node
        self.head = new_node
        self.length += 1
        print(self.length)
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
        leader = self.traverse_to_node(index - 1)
        follower = leader.next #holding_pointer

        new_node.previous = leader
        leader.next = new_node

        new_node.next = follower
        follower.previous = new_node

        self.length += 1
        return self.print_list()
    
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
        
        # Case: Remove head
        if index == 0:
            self.head = self.head.next
            # Only set previous if head still exists:
            if self.head:
                self.head.previous = None
                # If the list only had 1 element to begin with:
                # After: self.head = self.head.next -> you would get: self.head is None, so self.head.previous = None would give AttributeError: 'NoneType' object has no attribute 'previous'
            self.length -= 1
            # Update tail if list is now empty
            if self.length == 0:
                self.tail = None

            return self
        
        leader = self.traverse_to_node(index - 1)
        unwanted_node = leader.next
        updated_follower = unwanted_node.next

        leader.next = updated_follower

        # Case: Node to remove is NOT the head or tail
        if updated_follower:
            updated_follower.previous = leader

        # Case: Remove tail
        # If unwanted_node is the tail, then: unwanted_node.next is None
        # So: 
            # updated_follower = None
            # updated_follower.previous  # ❌ crash
        else:
            self.tail = leader

        self.length -= 1
        return self       

    # To visualise the LinkedList as an array:
    def print_list(self):
        list = []
        current_node = self.head
        while current_node is not None:
            list.append(current_node.value)
            current_node = current_node.next
        return list
    
myLinkedList = DoublyLinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16) 
myLinkedList.prepend(1)
myLinkedList.insert(2, 99) #[1, 10, 99, 5, 16]
myLinkedList.insert(20, 88) #[1, 10, 99, 5, 16, 88]
myLinkedList.remove(2) #[1, 10, 5, 16, 88]
print(myLinkedList.print_list()) 
