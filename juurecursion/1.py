def print1ToN(n):
    #code here
    if n <=1:
        n=1
        print(n,end=" ")
        return 0
    if n>1:
        print1ToN(n-1)
    print(n,end=" ")

def printNto1(n):
    if n <=1:
        n=1
        print(n,end=" ")
        return 0
    if n>0:
        print(n,end=" ")
        printNto1(n-1)
    
n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)