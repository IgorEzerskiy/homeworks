amount = int(input("Enter the amount of money: "))


def thousands(thousand: int):
    thousand //= 1000
    return thousand


def hundreds(hundred: int):
    hundred %= 1000
    return hundred


def tens(ten: int):
    ten %= 100
    return ten


ten_var = tens(amount)
hundred_var = hundreds(amount)

if amount % 1000:
    if amount > 100:
        if hundred_var == 500:
            print(f"You have: 1 bills 500 uah")
        elif hundred_var//100 == 6:
            print(f"You have: 1 bills 500 uah")
            print(f"You have: 1 bills 100 uah")
        else:
            if (hundred_var % 2 == 0) and (hundred_var < 500):
                if (hundred_var % 2 == 0) and (hundred_var != 100):
                    hundred_var //= 100
                    print(f"You have: {int(hundred_var / 2)} bills 200 uah")
                else:
                    print(f"You have: {int(hundred_var // 100)} bills 100 uah")
            elif (hundred_var % 2 == 0) and (hundred_var > 500):
                hundred_var -= 500
                hundred_var //= 100
                if hundred_var % 2 == 0:
                    print(f"You have: 1 bills 500 uah")
                    print(f"You have: {int(hundred_var / 2)} bills 200 uah")
                else:
                    i = hundred_var % 2
                    print(f"You have: 1 bills 500 uah")
                    print(f"You have: {i} bills 100 uah")
                    print(f"You have: {int((hundred_var / 2))} bills 200 uah")
    if tens(amount):
        if ten_var == 50:
            print(f"You have: 1 bills 50 uah")
        elif ten_var == 60:
            print(f"You have: 1 bills 50 uah")
            print(f"You have: 1 bills 10 uah")
        else:
            if (ten_var % 2 == 0) and (ten_var < 50):
                if (ten_var % 2 == 0) and (ten_var != 10):
                    ten_var //= 10
                    print(f"You have: {int(ten_var / 2)} bills 20 uah")
                else:
                    print(f"You have: {int(ten_var // 10)} bills 10 uah")
            elif (ten_var % 2 == 0) and (ten_var > 50):
                ten_var -= 50
                ten_var //= 10
                if ten_var % 2 == 0:
                    print(f"You have: 1 bills 50 uah")
                    print(f"You have: {int(ten_var / 2)} bills 20 uah")
                else:
                    i = ten_var % 2
                    print(f"You have: 1 bills 50 uah")
                    print(f"You have: {i} bills 10 uah")
                    print(f"You have: {int((ten_var / 2))} bills 20 uah")

    if thousands(amount):
        print(f"You have: {thousands(amount)} bills 1000 uah")
else:
    print(f"You have: {thousands(amount)} bills 1000 uah")
