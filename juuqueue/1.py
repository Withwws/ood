Q = []
input= input("Enter Input : ").split(",")

for i ,j in enumerate(input):
    
    s= j.split()
    if s[0] == "E":
        Q.append(s[1])
        print(len(Q))
    elif s[0] == "D":
        if len(Q) >0:
            print(Q.pop(0)+" 0")
        else:
            print("-1")
if len(Q) > 0:
    print(*Q)
else:
    print("Empty")
        