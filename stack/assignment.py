class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # 1. Push an element into the stack
    def push(self, new_node):
        if new_node is None:
            print("Node is not created")
            return
        new_node.next = self.top
        self.top = new_node

    # 2. Pop an element from the stack
    def pop(self):
        if self.isempty():
            print("stack is empty")
            return None
        else:
            temp = self.top
            print("Popped ELement:", temp.data)   
            self.top = self.top.next
            return temp                           

    # 3. Display elements of the stack (Q3)
    def display(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
    # 4. Reverse String using Stack
    def reverse_string(self, input_str):
        st = Stack()
        for char in input_str:
            st.push(Node(char))
        print(f"Original String: {input_str}")
        print("Reversed String: ", end="")
        while not st.isempty():
            temp = st.top        
            st.top = st.top.next
            print(temp.data, end="")
        print()

    # 5. Reverse Stack using another Stack 
    def reverse(self):
        if self.isempty():
            print("stack is empty")
            return
        st1 = Stack()
        st2 = Stack()
        while not self.isempty():
            temp = self.top        
            self.top = self.top.next
            st1.push(temp)
        while not st1.isempty():
            temp = st1.top
            st1.top = st1.top.next
            st2.push(temp)
        while not st2.isempty():
            temp = st2.top
            st2.top = st2.top.next
            self.push(temp)

    # Extra helper: print the stack
    def print(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next



s = Stack()

s.push(Node(1))
s.push(Node(2))
s.push(Node(3))
s.push(Node(4))
s.push(Node(100))
s.push(Node(200))
s.push(Node(300))

print("elements in the stack")
s.print()

s.pop()
s.pop()
print("elements in stack after pop")
s.print()

print("Display the elements in stack")
s.display()


print(" Reverse String using Stack ")
s.reverse_string("hello")


print(" Reverse Stack using another Stack ")
print("BEFORE:")
s.print()

s.reverse()

print("AFTER:")
s.print()