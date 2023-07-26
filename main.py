# main.py
from linkedlists.singly_linked_list import SinglyLinkedList
from linkedlists.singly_linked_list import Queue

def main():
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    # Create a singly linked list
    linked_list = SinglyLinkedList()

    # Insert elements from the data_list into the linked list
    for data in data_list:
        linked_list.insert(data)

    # Display the elements of the linked list
    linked_list.display()
 


#TASK 2
def main():
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    # Create a singly linked list
    linked_list = SinglyLinkedList()

    # Insert elements from the data_list into the linked list
    for data in data_list:
        linked_list.insert(data)

    # Display the elements of the linked list
    linked_list.display()

    # Find the maximum and minimum data in the linked list
    max_data, min_data = linked_list.find_max_min()
    print(f"Maximum data: {max_data}, Minimum data: {min_data}")

if __name__ == "__main__":
    main()

#TASK 2(ii)
def main():
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    # Create a singly linked list
    linked_list = SinglyLinkedList()

    # Insert elements from the data_list into the linked list
    for data in data_list:
        linked_list.insert(data)

    # Display the elements of the linked list
    linked_list.display()

    # Convert the linked list into a binary search tree using the given list [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    bst_root = linked_list.convert_to_bst([1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28])

    # Display the binary search tree
    print("Binary Search Tree:")
    print(bst_root)

if __name__ == "__main__":
    main()
    #TASK 3(ii)
# Testing Queueing operations
def main():
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    queue = Queue()
    for data in data_list:
        queue.enqueue(data)

    print("\nQueue:")
    queue.display()

    print("Dequeue:", queue.dequeue())

    print("Queue after dequeue:")
    queue.display()

    queue.sort_queue()
    print("\nSorted Queue:")
    queue.display()
    if __name__ == "__main__":
     main()