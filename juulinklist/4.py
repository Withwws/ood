class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class Linklisted:
    def __init__(self) -> None:
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_start(data)
        
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            node = Node(data)
            itr.next = node

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if self.head == None or self.get_length() <= index:
            raise Exception("invalid index")
        
        if index == 0:
            self.head = self.head.next
            return 
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index > self.get_length():
            raise Exception(f"this link listed have {self.get_length()} for now")

        if index == 0:
            self.insert_at_start(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1


    def show(self):
        ll = ""
        itr = self.head
        while itr:
            ll += str(itr.data) + "--->"
            itr = itr.next
        print(ll)

inp = input("Enter Input : ").split(',')
ll = Linklisted()
cursor = 0

for i, j in enumerate(inp):
    if j[0] == 'I':
        ll.insert_at(cursor, j[2:] + ' ')
        cursor += 1
    elif j == 'L':
        if cursor == 0:
            cursor += 1
        cursor -= 1
    elif j == 'R':
        if cursor == ll.get_length():
            cursor -= 1
        cursor += 1
    elif j == 'B':
        if cursor != 0:
            ll.remove_at(cursor - 1)
            cursor -= 1
    elif j == 'D':
        if cursor != ll.get_length():
            ll.remove_at(cursor)

itr = ll.head
while itr:
    if cursor == 0:
        print("| ", end = "")
    
    print(itr.data, end = "")
    cursor -= 1
    itr = itr.next

if cursor == 0:
    print("| ", end = "")