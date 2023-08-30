print(" *** String count ***")
x= list(input("Enter message : "))
u=0
l=0
uc =[]
lc=[]
for i in range(len(x)-1):
    if x[i]>='A' and x[i]<='Z':
        u+=1
        if x[i] not in uc:
            uc.append(x[i])
    if x[i]>='a' and x[i]<='z':
        l+=1
        if x[i] not in lc:
            lc.append(x[i])
uc.sort()
lc.sort()
uuc = '  '.join(uc)
llc = '  '.join(lc)
print("No. of Upper case characters :",u)
print("Unique Upper case characters :",uuc)
print("No. of Lower case Characters :",l)
print("Unique Lower case characters :",llc)
