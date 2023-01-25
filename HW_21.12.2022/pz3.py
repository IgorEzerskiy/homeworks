n = int(input("Write your number: "))
i = 1
dividers = ""

while i <= n:
    if n % i == 0:
        dividers += (str(i)+" ")
    i += 1
print(f"Number divisors {n}: {dividers}")
