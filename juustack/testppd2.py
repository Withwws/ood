print(" *** Rank score ***")
x = input("Enter ID and Score end with ID : ").split( )
print(x[0:len(x)-1])
print(x[len(x)-1])
id = x[len(x)-1]
x.pop()
dict = {}
i=0
while i in range(len(x)-1):
    dict[x[i]] = x[i+1]
    i+=2
for key in dict:
    dict[key] = float(dict[key])
print(dict)
sl = list(dict.values())
sl.sort(reverse=True)
sc = dict[id]
a=1
for j in range(len(sl)-1):
    if sl[j] == sc:
        print(a)
    a+=1