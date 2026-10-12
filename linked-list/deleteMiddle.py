# write a function to find middle no and delete

class Node:
    def __init__(self,val):
        self.head = val
        self.next = None

class linkedList:
    def __init__(self):
     self.head = None

    def append(self,new_node):
       if (self.head ==None):
          self.head = new_node
       else:
           temp=self.head
           while(temp.next) :
                temp=temp.next
           temp.next = new_node
           

        


    def findmid_del(self):
       temp=temp1=self.head
       prev=None
       while temp1 and temp.next:
           prev = temp
           temp = temp.next
           temp1=temp1.next.next
           print("Middle Node:", temp.data)
           prev.next=temp.next
           temp=None

    def delFIrst_last(self):
        temp1=self.head #delete first
        temp1=None      #delete first
        prev =None
        temp=self.head=self.head.next 
        while (temp.next):
            prev=temp
            temp=temp.next
        prev.next=None   #delete last
        temp=None        #delete last

        # delete alternate nodes
    def delAlternate(self):
        prev=self.head
        temp=self.head.next
        while prev and temp:
            prev.next= temp.next
            temp=None #delete the node
            prev = prev.next
            if prev:
                temp=prev.next
    def concatenate(self):
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next = list2.head    

    
    
    
    def print(self):
        print("list elements:") 
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next

list= linkedList()
list2=linkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.append(Node(55))
list.print()
list.findmid_del()
list.print()
list.delFIrst_last()
list.print()
list.delAlternate()
list.print()            

n1=Node(50)
n2=Node(60)
n3=Node(70)
list2.append(n1)
list2.append(n2)
list2.append(n3)
list2.append(Node(80))
list2.append(Node(75))
list2.print()         
list.concatenate()