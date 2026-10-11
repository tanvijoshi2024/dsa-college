class Node:
    def __init__(self,val):
        self.data= val
        self.next=None
class linkedList:
    def __init__(self):
        self.head =None
 #create a node
    def append(self, new_node):
        if (self.head == None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next) :
                           temp=temp.next
            temp.next = new_node #appending new node      

   # 2. Traverse and print the node values
    def traverse(self):
        if (self.head == None):
            print("The list is empty.")
            return
        temp = self.head
        while (temp):
            print(temp.data, end=" " if temp.next else "\n")
            temp = temp.next
        

    # 3. Insert node at a specific position 
    def insert_at_position(self, pos,val):
        new_node = Node(val)
        
        # If inserting at the very front (position 1)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            p=1
            while(p!=pos -1 and temp.next != None):
                temp=temp.next
                p+=1
            new_node.next = temp.next
            temp.next=new_node
        

    # 4. Find Middle node and print its value
    def find_middle(self):
        if (self.head == None):
            print("The list is empty.")
            return
            
        slow = self.head
        fast = self.head
        
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            
        print(f"Middle node value: {slow.data}")

    # 5. Delete node (by value)
    def delete_node(self,val):
        temp = self.head
        if temp ==None:
            print("list is empty")
            return
        
        if temp.data ==val:
            self.head = self.head.next
            return
        prev = None
        while(temp and temp.data!=val):
            prev = temp
            temp = temp.next
        if temp==None:
            print("Value is not there in the list")
            return 
        prev.next=temp.next       
        
       
    # 6. Reverse list
    def reverse(self):
        prev = None
        current = self.head
        
        while (current):
            next_node = current.next  
            current.next = prev     
            prev = current           
            current = next_node       
            
        self.head = prev
        print("List reversed.")

    # 7. Calculate the sum of every two consecutive node values
    def sum_consecutive(self):
        if (self.head == None or self.head.next == None):
            print("Not enough nodes for consecutive sums.")
            return
            
        temp = self.head
        print("Sums of consecutive nodes:")
        while temp != None and temp.next != None:
            pair_sum = temp.data + temp.next.data
            print(f"({temp.data} + {temp.next.data}) = {pair_sum}")
            temp = temp.next

    def print(self):
       if (self.head ==None):
           print("empty list")
           return
       temp = self.head
       result=[]
       while temp:
           result.append(str(temp.data))
           temp = temp.next
           print(" ".join(result))
           
l1=linkedList()
l1.append(Node(10))
l1.append(Node(20))
l1.append(Node(30))
print("1) Traverse:")
l1.traverse()
print("2) Print")
l1.print()
print("2) Print")
l1.print()
print("3) Insert 90 at position 2")
l1.insert_at_position(90,2)
l1.print()
print("3b) Insert 33 at position 7")
l1.insert_at_position(33,7)
l1.print()
print("4) Middle")
l1.find_middle()
print("5) Delete 30:")
l1.delete_node(20)
l1.print()
print("6) Reverse:")
l1.reverse()
l1.print()
print("7) Sum consecutive:")
l1.sum_consecutive()


    

        