class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            self.tail = new_node
            new_node.previous = cur

    def addHead(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(item)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, pos, item):
        count = 0
        new_node = Node(item)
        if self.head is None:
            self.addHead(item)
        elif pos > int(self.size()):
            self.append(item)
        elif pos < 0 and pos*-1 > int(self.size()):
            self.addHead(item)
        elif pos < 0:
            current = self.tail 
            count = 0
            while self.tail:
                if count == pos:
                    new_node.previous = current
                    new_node.next = current.next
                    if current.next:
                        current.next.previous = new_node
                    current.next = new_node
                    break
                current = current.previous
                count -= 1
        else:
            current = self.head
            while current:
                if pos-1 == count:
                    new_node.previous = current
                    new_node.next = current.next
                    if current.next:
                        current.next.previous = new_node
                    current.next = new_node
                    break
                current = current.next
                count += 1

    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.value == item:
                return "Found"
            cur = cur.next
        return "Not Found"

    def index(self, item):
        cur = self.head
        idx = 0
        while cur != None:
            if cur.value == item:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def size(self):
        size = 0
        cur = self.head
        while cur != None:
            cur = cur.next
            size += 1
        return size

    def pop(self, pos):
        if self.isEmpty() or pos < 0 or pos >= self.size():
            return "Out of Range"

        if pos == 0:
            removed_value = self.head.value
            self.head = self.head.next
        else:
            prev = None
            cur = self.head
            count = 0
            while cur is not None and count < pos:
                prev = cur
                cur = cur.next
                count += 1
            removed_value = cur.value
            prev.next = cur.next

        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())