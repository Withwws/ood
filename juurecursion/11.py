def print1ToN(n):
    #code here
    print(n-(n-1),print1ToN())

def printNto1(n):
    #code here
    pass

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)