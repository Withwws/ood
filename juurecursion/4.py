pat = 0

def pantip(money, n, arr, path):
    global pat
    if money == 0:
        print(*path)
        pat += 1
        return
    elif n >= len(arr) or money < 0:
        return
    elif money > 0:
        path.append(arr[n])
        pantip(money - arr[n], n + 1, arr, path)
        path.pop()
    pantip(money, n + 1, arr, path)

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pat))