print(" *** Summation of each digit ***")
s=int(input("Enter a positive number : "))
j=0
while s>0:
    a = s%10
    j +=a
    s = s//10
print("Summation of each digit = ",j)