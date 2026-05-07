class Node:
    """
    A fundamental Node Class for building a Linked List.
    Holds a 'value' and a 'next' Pointer.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    The LinkedList Class that manages the Nodes.
    It keeps track of the 'head' (the first Node in the chain).
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Creates a new Node and appends it to the end of the Linked List.
        """
        new_node = Node(value)

        # If the list is entirely empty, the new Node becomes the Head
        if self.head == None:
            self.head = new_node
            return

        # If the list is not empty, traverse to the last Node
        current_node = self.head
        
        # Traverse the list by following the Pointers until next is None
        while current_node.next != None:
            current_node = current_node.next

        # Link the last Node's next Pointer to the newly created Node
        current_node.next = new_node


if __name__ == "__main__":
    # --- EXECUTION & TESTING ---
    my_list = LinkedList()
    
    # Appending values to the Linked List
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)

    # Printing the values to verify the Pointer connections
    print("[*] Linked List Append Test Started...\n")
    print(f"> Head Node: {my_list.head.value}")
    print(f"> Second Node: {my_list.head.next.value}")
    print(f"> Third Node: {my_list.head.next.next.value}")
    print("\n[+] Append operations successful!")