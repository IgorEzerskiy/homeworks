"""
if (умова) дія
if (умова) (блок дій в кілька рядків)
if (умова) (блок дій в кілька рядків) else дія
if (умова) (блок дій в кілька рядків) else (блок дій в кілька рядків)
if (умова) (блок дій в кілька рядків) elif дія else (блок дій в кілька рядків)
if (умова) (блок дій в кілька рядків) elif (блок дій в кілька рядків) else (блок дій в кілька рядків)
"""
i = int(input("Write tour number: "))

print("Out from 1: ")
if i == i:
    print(str(i) + "\n")
print("Out from 2: ")
if i <= 5:
    i += 5
    print(str(i) + "\n")
print("Out from 3: ")
if i >= 10:
    i -= 3
    print(str(i) + "\n")
else:
    print(str(i) + "\n")
print("Out from 4: ")
if i <= 15:
    i -= 6
    print(str(i) + "\n")
else:
    while i <= 25:
        i += i
    print(str(i) + "\n")
print("Out from 5: ")
if (i >= 15) and (i <= 30):
    i *= 3
    print(str(i) + "\n")
elif (i >= 30) and (i < 35):
    while i <= 35:
        i += i
    print(str(i) + "\n")
print("Out from 6: ")
if ((i >= 35) and (i <= 40)) or ((i > 40) and (i <= 70)):
    i *= 3
    print(str(i) + "\n")
elif (i >= 70) and (i < 100):
    while i <= 99:
        i += i
    print(str(i) + "\n")
else:
    i = 100
    print(str(i) + "\n")
