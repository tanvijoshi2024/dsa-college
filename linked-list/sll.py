#single linked list
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self, new_node):
          if (self.head==None):
              self.head=new_node  
          else:
              temp=self.head
              while(temp.next) :
                  temp=temp.next
                  temp.next = new_node #appending new node               
    def print(self):
        count=0
        temp=self.head
        while temp.next:
            print(temp.data)
            temp=temp.next.next
        if temp:
            print(temp.data)    

list=Linkedlist()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.append(Node(55))

list.print()
