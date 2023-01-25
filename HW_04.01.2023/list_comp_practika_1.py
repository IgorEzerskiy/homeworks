from random import randint
n = randint(1, 21)
m = randint(1, 21)

a = [[randint(1, m) for j in range(m)] for i in range(n)]
b = max([sum(i) for i in a])

for i in a:
    print(i)
print(f"Max sum in line: {b} \n")