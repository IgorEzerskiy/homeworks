number = abs(int(input("Write your number: ")))
number = str(number)
digits = []
factor = 1

for i in range(len(number)):
    digits.append(number[i])

for index in enumerate(digits[::-1]):
    if index == 0:
        print(f"Digit {index[0]+1}: {digits[index[0]]}, factor: {factor}")
    elif index != 0:
        factor *= 10
        print(f"Digit {index[0]+1}: {digits[index[0]]}, factor: {factor}")
