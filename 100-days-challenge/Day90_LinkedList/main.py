class Node:
    """
    A fundamental Node class for building a Linked List.
    Each Node holds a 'value' and a 'next' pointer to the subsequent Node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None  # Initially, the pointer points to nowhere (None)


if __name__ == "__main__":
    # --- EXECUTION & LINKING ---
    
    # 1. Create two independent Node objects in memory
    node1 = Node(10)
    node2 = Node(20)
    
    # 2. Link them together: Set node1's pointer to the memory address of node2
    node1.next = node2
    
    # --- TEST OUTPUTS ---
    print("[*] Linked List Test Started...\n")
    print(f"> Node 1 Value: {node1.value}")
    
    # Accessing node2's value by traversing through node1's pointer!
    print(f"> Node 2 Value (Accessed via Node 1's pointer): {node1.next.value}")
    print("\n[+] Linking successful!")