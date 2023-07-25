# linkedlists/singly_linked_list.py
from nodes.node import Node
from binarytree import build  

#TASK 1
class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def insert(self, data):
        """
        Insert a new element at the end of the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """
        Display the elements of the linked list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)
 #JUST TO CHECK FOR THE LENGTH OF THE LINKED LIST
    def length(self):
        """
        Calculate the length of the linked list.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

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
