class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
         self.top = None
         self.next = None

    def isempty(self):
        return self.top is None

    # push an element into the stack
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node

# pop an element from the stack
    def pop(self):
        if self.isempty():
                    print("stack is empty")
        else:
             temp=self.top
             print("Popped ELement:", temp.data)
             self.top=self.top.next
             temp=None

    def reverse(self):
        temp=self.top
        while temp:
            st.push(Node(temp.data))
            temp=temp.next  
                 

    def print(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            while(temp):
                print(temp.data)
                temp=temp.next

s=Stack()
st=Stack()
s.push(Node(1))
s.push(Node(2))
s.push(Node(3))
s.push(Node(4))
s.push(Node(100))
s.push(Node(200))
s.push(Node(300))
print("elements in stack:")
s.print()
s.pop()
s.pop()
print("after pop elements in the stack are")
s.print()

#reverse an element
s.reverse()
print("after reversing the stack elements are")
st.print()
