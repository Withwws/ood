class Stack:

    def __init__(self, lst = []):
        self.items = lst

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

m,n = int(m),int(n)

s = s.split(',')
for i, j in enumerate(s):
    s[i] = int(j)
if s == [0]:
    s = []

if o == 'arrive':
    if n in s:
        print(f"car {n} already in soi")
    elif len(s) >= m:
        print(f"car {n} cannot arrive : Soi Full")
    else:
        print(f"car {n} arrive! : Add Car {n}")
        s.append(n)
else:
    if len(s) == 0:
        print(f"car {n} cannot depart : Soi Empty")
    elif n not in s:
        print(f"car {n} cannot depart : Dont Have Car {n}")
    else:
        print(f"car {n} depart ! : Car {n} was remove")
        s.remove(n)

print(s)