class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    # create a node
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            new_node.next=self.head 
        else:
            temp = self.head
            while(temp.next!=self.head):
                temp = temp.next
            temp.next = new_node  # appending new node
            new_node.next=self.head 


    # 3. Insert node at a specific position
    def insert(self, new_node,pos):
        # If inserting at the very front (position 1)
        if pos == 1:
            temp=self.head
            while(temp.next != self.head):#find last node
                temp=temp.next
            new_node.next=self.head    
            self.head = new_node
            temp.next=self.head
        else:
            p=1
            temp = self.head
            while(p!=(pos-1) ):
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node
       

   

    # 5. Delete node (by value)
    def delete(self, val):
        temp = self.head
        prev=None
        if temp.data == val:
            while(temp.next!=self.head):
                temp=temp.next
            self.head = self.head.next
            temp.next=self.head
        else:    
            while( temp.data != val and temp):
                prev = temp
                temp = temp.next
                if temp == None:
                    print("Value is not there in the list")
                    return 
            prev.next = temp.next
            temp=None
       



    def print(self):
       print()
       print("list of elements:")
       temp=self.head
       while(True):
           print(temp.data,end=" ")
           temp=temp.next
           if temp==self.head:
               break



# ==========================================
# Main Program (using your original test format)
# ==========================================
l1 = linkedList()

# Create the list
l1.append(Node(10))
l1.append(Node(20))
l1.append(Node(30))
l1.append(Node(40))
l1.insert(Node(38),7)
l1.print()
l1.delete(20)
l1.print()

