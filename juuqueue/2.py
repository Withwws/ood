input = list(input("Enter people : "))

q_1 = []
q_2 = []
i = 0
i_q2 = 0

while len(input) > 0:
    if i > 0 and i % 3 == 0:
        q_1.pop(0)
    if i_q2 > 0 and i_q2 % 2 == 0:
        q_2.pop(0)
    if len(q_1) < 5:
        q_1.append(input[0])
        input.pop(0)
    elif len(q_1) >= 5:
        q_2.append(input[0])
        input.pop(0)
    if len(q_2) != 0:
        i_q2 += 1
    i += 1
    print(f"{i} {input} {q_1} {q_2}")