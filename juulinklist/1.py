class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head is None:
            self.addHead(item)
        else:
            link = self.head
            while link.next:
                link = link.next
            node  = Node(item)
            link.next = node

    def addHead(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def search(self, item):
        link = self.head
        while link:
            if link.value == item:
                return "Found"
            link = link.next
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
        link = self.head
        count = 0
        while link:
            link = link.next
            count += 1
        return count

    def pop(self, pos):
        if self.head == None or self.size() <= pos:
            return "Out of Range"
        
        if pos == 0:
            self.head = self.head.next
            return "Out of Range"
        
        count = 0
        itr = self.head
        while itr:
            if count == pos - 1:
                itr.next = itr.next.next
                return "Success"
            itr = itr.next
            count += 1
        else:return "Out of Range"
            
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)