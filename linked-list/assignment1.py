# Create a Singly Linear Linked List with following operations
class Node:
    def __init__(self, val):
        self.data = val      
        self.next = None      

class LinkedList:
    def __init__(self):
        self.head = None    

    # 1. Create Linked List )
    def append(self, val):
        new_node = Node(val)  
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:     
            temp = temp.next
        temp.next = new_node  

    # 2. Traverse and print the node values
    def traverse(self):
        if self.head is None:
            print("The list is empty.")
            return
        
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements))

    # 3. Insert node at a specific position 
    def insert_at_position(self, val, position):
        new_node = Node(val)
        
        # If inserting at the very front (position 1)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        for _ in range(position - 2):
            if temp is None:
                print("Position out of bounds.")
                return
            temp = temp.next
            
        if temp is None:
            print("Position out of bounds.")
            return
            
       
        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {val} at position {position}.")

    # 4. Find Middle node and print its value
    def find_middle(self):
        if self.head is None:
            print("The list is empty.")
            return
            
        slow = self.head
        fast = self.head
        
        # Fast moves 2 steps, slow moves 1 step
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        print(f"Middle node value: {slow.data}")

    # 5. Delete node (by value)
    def delete_node(self, key):
        temp = self.head
        
       
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                print(f"Deleted node with value {key}.")
                return
                
      
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            
        # If the value wasn't found
        if temp is None:
            print(f"Value {key} not found in the list.")
            return
            
       
        prev.next = temp.next
        print(f"Deleted node with value {key}.")

    # 6. Reverse list
    def reverse(self):
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next  
            current.next = prev     
            prev = current           
            current = next_node       
            
        self.head = prev
        print("List reversed.")

    # 7. Calculate the sum of every two consecutive node values
    def sum_consecutive(self):
        if self.head is None or self.head.next is None:
            print("Not enough nodes for consecutive sums.")
            return
            
        temp = self.head
        print("Sums of consecutive nodes:")
        while temp is not None and temp.next is not None:
            pair_sum = temp.data + temp.next.data
            print(f"({temp.data} + {temp.next.data}) = {pair_sum}")
            temp = temp.next


list=LinkedList()
n1 =Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(40)
list.traverse()
print("insert at position")
list.insert(Node(100),1)
list.traverse()
list.insert(Node(66),4)
list.traverse()
list.find_middle()
list.traverse()
list.delete(30)
list.traverse()
list.reverse()
list.traverse()
list.sum_consecutive()
list.traverse()