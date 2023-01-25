"""Придумати власні приклади на альтернативні варіанти if і активне використання булевої алгебри."""
num1 = int(input("Write number 1: "))
num2 = int(input("Write number 2: "))

if num1 > num2:
    num2 **= 2
elif num1 < num2:
    num1 /= 2
if (num1 + num2) >= (num2 * (num1 -2)) or ((num1 * num2) < (num1**2)):
    print("How it works?")
else:
    print("It doesnt work!")
if ((num1%2)>(num2%3)) or ((num2*2)<(num1**2)):
    print("Looks very strange O_O")
elif ((num1%5)<(num2%3)) or ((num2**2)>(num1**3)):
    print("Looks even weirder O_o")
else:
    print("Oh, it's okay :)")
