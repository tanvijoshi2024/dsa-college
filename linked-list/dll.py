class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def   append(self,new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        else:
            self.head=new_node
    def print(self):
        temp=self.head
        print("list of elements:")            
        while temp:
            print(temp.data," ")

list=linkedList()
list.append(Node(10))
list.append(Node(15))
list.append(Node(20))
list.append(Node(25))
list.print()
