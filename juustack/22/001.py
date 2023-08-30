class Stack(object):
    def __init__ (self):
        self.item = []
    
    def push(self,item):
        self.item.append(item)
    # push the element into the list in the last index
        
    def pop(self):
        return self.item.pop()
        
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
        
    def size(self): 
        if self.item:
            return len(self.item)
        else:
            return 0
        
    def isempty(self):
        if self.item == []:
            return True
        else:
            return False
        
print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.item)

while not s.isempty():

    s.pop()

print(s.size(),"Data in stack : ",s.item)