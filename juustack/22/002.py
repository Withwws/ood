input = input("Enter Input : ").split(",")

stack = []

for i, j in enumerate(input):
    if len(stack) == 0:
        stack.append(j)
    else:
        while int(j.split()[0]) > int(stack[-1].split()[0]):
            print((stack.pop()).split()[1])
            if len(stack) == 0:
                break
        stack.append(j)