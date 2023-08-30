class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)

class Linkedlist:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
    
    def __len__(self):
        return self.length

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

    def count(self, Linkedl):
        cur = Linkedl.head
        count = 0
        while cur is not Linkedl.tail:
            count += 1
            cur = cur.next
        return count
    
    def append(self, item):
        cur = self.head
        while cur.next is not self.tail:
            cur = cur.next
        node = Node(item, cur, self.tail)
        self.tail.prev = node
        node.next = self.tail
        node.prev = cur
        cur.next = node
        self.length += 1

    def addHead(self, item):
        cur = self.head.next
        node = Node(item, self.head, self.head.next)
        cur.prev = node
        self.head.next = node
        self.length += 1
    



def createLL(LL: list):
    LinkedL = Linkedlist()  
    for i in LL:
        LinkedL.append(i)
    return LinkedL

def printLL(head):
    return head

def SIZE(head):
    return head.length

def bottomup(head:Linkedlist, count_bottomup: int,size ,debottom = False):
    if debottom == True:
        count_bottomup = size - count_bottomup
    LL = Linkedlist()
    count = 0 
    cur = head.head
    
    while cur.next is not head.tail:
        if count >= count_bottomup:
            LL.append(cur.next.value)
        count += 1
        cur = cur.next
    
    cur = head.head
    count = 0
    while cur.next is not head.tail:
        if count < count_bottomup:
            LL.append(cur.next.value)
        count += 1
        cur = cur.next

    return LL

def riffle(head:Linkedlist,count_riffle:int):
    LL1 = Linkedlist()
    LL2 = Linkedlist()
    LL3 = Linkedlist()
    
    count = 0
    cur = head.head
    
    while cur.next is not head.tail:
        if count < count_riffle:
            LL1.append(cur.next.value)
        cur = cur.next 
        count += 1
        
    count = 0 
    cur = head.head
    
    while cur.next is not head.tail:
        if count >= count_riffle:
            LL2.append(cur.next.value)
        cur = cur.next
        count += 1
    
    lenL1, lenL2 = len(LL1), len(LL2)
    count1 ,count2 = 0, 0
    
    curLL1, curLL2 = LL1.head , LL2.head
    
    while count1 < lenL1 and count2 < lenL2:
        LL3.append(curLL1.next)
        count1 += 1
        curLL1 = curLL1.next
        
        LL3.append(curLL2.next)
        count2 += 1
        curLL2 = curLL2.next
        
    while count1 < lenL1:
        LL3.append(curLL1.next)
        count1 += 1
        curLL1 = curLL1.next
    
    while count2 < lenL2:
        LL3.append(curLL2.next)
        curLL2 = curLL2.next
        count2 += 1
        
    return LL3
    
def deriffle(head: Linkedlist, count_riffle:int, size):
    LL1 = Linkedlist()
    LL2 = Linkedlist()
    LL3 = Linkedlist()
    
    countLL1 = 0
    countLL2 = 0
    len1 = count_riffle
    len2 = size - count_riffle
    
    addTail = False
    
    if len1 > len2:
        addTail = True
    
    count = 0
    cur = head.head
    
    while cur.next is not head.tail:
        
        if countLL1 < len1 and countLL2 < len2:
            if count % 2 == 0:
                LL1.append(cur.next.value)
                countLL1 += 1
            else:
                LL2.append(cur.next.value)
                countLL2 += 1
        else:
            if addTail and countLL2 >= len2:
                LL1.append(cur.next.value)
            elif not addTail and countLL1 >= len1:
                LL2.append(cur.next.value)
                countLL2 += 1
                
        cur = cur.next
        count += 1
    
    LL = Linkedlist()
    cur = LL1.head
    while cur.next is not LL1.tail:
        LL.append(str(cur.next.value))
        cur = cur.next
    
    cur = LL2.head
    while cur.next is not LL2.tail:
        LL.append(str(cur.next.value))
        cur = cur.next
    
    return LL
            
        



def scarmble(head:Linkedlist, b, r, size):
    count_bottom_up = int((size*b)/100)
    count_riffle = int((r*size)/100)
    
    LL1 = bottomup(head, count_bottom_up,size, False)
    print(f'BottomUp {b:.3f} % : {LL1}')
    LL2 = riffle(LL1,count_riffle)
    print(f'Riffle {r:.3f} % : {LL2}')
    LL3 = deriffle(LL2, count_riffle, size)
    print(f'Deriffle {r:.3f} % : {LL3}')
    LL4 = bottomup(LL3, count_bottom_up, size, True)
    print(f'Debottomup {b:.3f} % : {LL4}')
    
    
    

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)