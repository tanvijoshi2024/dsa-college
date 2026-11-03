class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.isempty():
            return None
        temp = self.top
        self.top = self.top.next
        return temp

class LQueue:
    def __init__(self):
        self.front = self.rear = None

    # 1. Enqueue an element into the queue
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    # 2. Dequeue an element from the queue
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        temp = self.front
        print("delete node", temp.data)
        self.front = self.front.next
        if self.front == None:         
            print("Queue is empty now")
            self.rear = None
        return temp

    # 3. Display 
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

  

    # 4. Reverse the queue using stack
    def reverse_queue(self):
        if self.front is None:
            print("Queue is empty")
            return
        st = Stack()
        while self.front is not None:
            temp = self.front
            self.front = self.front.next
            st.push(temp)
        self.rear = None
        while not st.isempty():
            self.enqueue(st.pop())

    # 5. Merge two queues into one
    def merge(self, other):
        merged = LQueue()
        temp = self.front
        while temp:
            merged.enqueue(Node(temp.data))
            temp = temp.next
        temp = other.front
        while temp:
            merged.enqueue(Node(temp.data))
            temp = temp.next
        return merged

    # 6. Check if two queues are identical
    def is_identical(self, other):
        p = self.front
        q = other.front
        while p is not None and q is not None:
            if p.data != q.data:
                return False
            p = p.next
            q = q.next
        return p is None and q is None

    
    def print(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


que = LQueue()
que.enqueue(Node(23))
que.enqueue(Node(63))
que.enqueue(Node(78))
que.enqueue(Node(20))

# calls made through print()
print("Enqueue operations:")
que.print()

print("Dequeue operations:")
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.print()

print(" Reverse the queue using stack")
q = LQueue()
q.enqueue(Node(1))
q.enqueue(Node(2))
q.enqueue(Node(3))
q.enqueue(Node(4))
print("Before reverse:")
q.print()
q.reverse_queue()
print("After reverse:")
q.print()

print(" Merge two queues into one")
q1 = LQueue()
q2 = LQueue()
q1.enqueue(Node(10))
q1.enqueue(Node(20))
q1.enqueue(Node(30))
q2.enqueue(Node(40))
q2.enqueue(Node(50))
print("Queue 1:")
q1.print()
print("Queue 2:")
q2.print()
merged = q1.merge(q2)
print("Merged queue:")
merged.print()

print(" Check if two queues are identical")
a = LQueue()
b = LQueue()
a.enqueue(Node(1))
a.enqueue(Node(2))
a.enqueue(Node(3))
b.enqueue(Node(1))
b.enqueue(Node(2))
b.enqueue(Node(3))
print("a == b ?", a.is_identical(b))

c = LQueue()
c.enqueue(Node(1))
c.enqueue(Node(2))
c.enqueue(Node(4))
print("a == c ?", a.is_identical(c))

d = LQueue()
d.enqueue(Node(1))
d.enqueue(Node(2))
print("a == d ?", a.is_identical(d))