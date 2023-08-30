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
    link, s = self.head, str(self.head.value) + " "
    while link.next != None:
      s += str(link.next.value) + " "
      link = link.next
    return s

  def isEmpty(self):
    return self.head == None

  def append(self, item):
    new_node = Node(item)
    if self.head == None:
      self.head = new_node
    else:
      link = self.head
      while link.next != None:
        link = link.next
      link.next = new_node

  def addHead(self, item):
    new_node = Node(item)
    new_node.next = self.head
    self.head = new_node

  def search(self, item):
    link = self.head
    while link != None:
      if link.value == item:
        return "Found"
      link = link.next
    return "Not Found"

  def index(self, item):
    link = self.head
    idx = 0
    while link != None:
      if link.value == item:
        return idx
      link = link.next
      idx += 1
    return -1

  def size(self):
    size = 0
    link = self.head
    while link != None:
      link = link.next
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
      link = self.head
      count = 0
      while link is not None and count < pos:
        prev = link
        link = link.next
        count += 1
      removed_value = link.value
      prev.next = link.next

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
    print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
          "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
