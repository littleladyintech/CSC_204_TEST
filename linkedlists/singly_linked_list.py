# linkedlists/singly_linked_list.py
from nodes.node import Node
from binarytree import build  

#TASK 1
class SinglyLinkedList:
    def __init__(self):
        #Initialize an empty singly linked list.
        self.head = None

    def insert(self, data):
    #Insert a new element at the end of the linked list.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        #Display the elements of the linked list.
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    # TASK 2
    def find_max_min(self):
        """
        Find and display the maximum and minimum data in the linked list.
        Returns a tuple containing (maximum, minimum).
        """
        if self.head is None:
            return None, None

        current = self.head
        max_data = self.head.data
        min_data = self.head.data

        while current:
            if current.data > max_data:
                max_data = current.data
            if current.data < min_data:
                min_data = current.data
            current = current.next

        return max_data, min_data
    
    #TASK 2(ii)

    def convert_to_bst(self, lst):
        """
        Converts the linked list into a binary search tree using the elements from the given Python list.
        Returns the root node of the binary search tree.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next

        # Merge the elements from the linked list and the given Python list
        elements += lst

        # Sort the elements in ascending order
        elements.sort()

        # Build the binary search tree
        root = build(elements)

        return root
    #Implementing a binary search algorithm
    def binary_search(self, search_value):
        # Sort the linked list using Python's built-in sorting function
        sorted_list = []
        current = self.head
        while current:
            sorted_list.append(current.data)
            current = current.next
        sorted_list.sort()

        # Binary search on the sorted list
        low, high = 0, len(sorted_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_list[mid] == search_value:
                return mid
            elif sorted_list[mid] < search_value:
                low = mid + 1
            else:
                high = mid - 1

        return -1
#Implementing Queue using a Singly Linked List

class Queue:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def enqueue(self, data):
        self.sll.insert(data)

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.sll.head.data
        self.sll.head = self.sll.head.next
        return data

    def display(self):
        self.sll.display()

    def is_empty(self):
        return self.sll.head is None
#Sort the Queue
    def sort_queue(self):
        # Extract elements from the queue
        elements = []
        while not self.is_empty():
            elements.append(self.dequeue())

        # Sort the elements
        elements.sort()

        # Re-enqueue the sorted elements
        for element in elements:
            self.enqueue(element)
