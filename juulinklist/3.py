class Node:
    def __init__(self, value, prev=None, next=None) -> None:
        self.value = value
        self.prev  = prev
        self.next = next
        
    def __str__(self) -> str:
        return str(self.value)

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node(None,None,None)
        self.tail = Node(None,None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
    
    def isEmpty(self):
        return self.length == 0
    
    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, []
        while cur.next is not self.tail:
            s.append(str(cur.next.value))
            cur = cur.next
        s = " ".join(s)
        s += " "
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, []
        while cur.prev is not self.head:
            s.append(str(cur.prev.value))
            cur = cur.prev
        s = " ".join(s)
        return s
    
    def append(self, item):
        cur = self.head
        
        while cur.next is not self.tail:
            cur = cur.next
        node = Node(item, cur, self.tail)
        self.tail.prev = node
        cur.next = node
        self.length += 1
        
    def addHead(self, item):
        cur = self.head.next
        node = Node(item, self.head, cur)
        cur.prev = node
        self.head.next = node
        self.length += 1

inp = input("Enter Input (L1,L2) : ").split(" ")

data1 = inp[0].split("->")
data2 = inp[1].split("->")
l1 = DoublyLinkedList()
l2 = DoublyLinkedList()

for i in data1:
    l1.append(i)

for i in data2:
    l2.append(i)

print("L1    : "+ str(l1))
print("L2    : "+ str(l2))

def merge(l1:DoublyLinkedList, l2:DoublyLinkedList):
    reverse = l2.reverse().split(" ")
    for i in reverse:
        l1.append(i)
    print(f"Merge : " + str(l1))
    
      
merge(l1, l2)