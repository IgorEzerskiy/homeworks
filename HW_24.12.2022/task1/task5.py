ten_uah = 10
twenty_uah = 10
fifty_uah = 10
hundred_uah = 10
numbers_of_banknotes = 0  # number of banknotes of {maximum_denomination} hryvnia
maximum_denomination = 0  # the maximum denomination that the program gives out cash in multiples of 1000

amount = int(input("Enter the amount of money in multiples of 10: "))
maximum_denomination = int(input(f"What denominations would you like to give out a multiple of 1000?\n "
                                 f"Available denominations: 100uah, 200uah, 500uah, 1000uah\n"
                                 f"Write your amount: "))


def hundreds(hundred: int):
    hundred %= 1000
    return hundred


def tens(ten: int):
    ten %= 100
    return ten


if amount % 10:
    print("Enter the amount of money in multiples of 10!!!")
else:
    ten_var = tens(amount)
    if ten_var:
        while ten_var:
            ten_uah -= 1
            ten_var -= 10
        amount -= (10-ten_uah)*10
        print(f"You have: {10-ten_uah} bills 10 uah")
    elif ten_var == 0:
        ten_uah -= 10
        amount -= 100
        print(f"You have: {10 - ten_uah} bills 10 uah")
    hundred_var = hundreds(amount)
    while hundred_var:
        if twenty_uah:
            twenty_uah -= 1
            hundred_var -= 20
            amount -= 20
        elif fifty_uah:
            fifty_uah -= 1
            hundred_var -= 50
            amount -= 50
        elif hundred_uah or hundred_var:
            hundred_uah -= 1
            hundred_var -= 100
            amount -= 100
    print(f"You have: {10 - twenty_uah} bills 20 uah")
    if fifty_uah != 10:
        print(f"You have: {10 - fifty_uah} bills 50 uah")
    while amount:
        numbers_of_banknotes += 1
        amount -= maximum_denomination
    if hundred_uah != 10:
        print(f"You have: {10-hundred_uah} bills 100 uah")
    print(f"You have: {numbers_of_banknotes} bills {maximum_denomination} uah")
