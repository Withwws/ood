print("*** multiplication or sum ***")
x,y=input("Enter num1 num2 : ").split( )
x=int(x)
y=int(y)
if x*y >1000:
    print("The result is",x+y)
else:
    print("The result is",x*y)