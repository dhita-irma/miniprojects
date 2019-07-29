# Change Return Program - The user enters a cost and then the amount of money given.
# The cost has to be lower than 2000.
# The program will figure out the change and the number of
# 100, 200, and 500, and 1000 needed for the change.

cost = int(input("Enter the cost: "))
money_given = int(input("Enter the money given: "))


def change(cost, money_given):
    change_amount = money_given - cost
    one_thousand_bill = 0
    five_hundred_bill = 0
    two_hundred_bill = 0
    one_hundred_bill = 0

    print(f"The change amount would be {change_amount}:")

    if change_amount > 0:
        while change_amount >= 1000:
            change_amount -= 1000
            one_thousand_bill += 1
        while change_amount >= 500:
            change_amount -= 500
            five_hundred_bill += 1
        while change_amount >= 200:
            change_amount -= 200
            two_hundred_bill += 1
        while change_amount >= 100:
            change_amount -= 100
            one_hundred_bill += 1

        print(f"{one_thousand_bill} one thousand bill(s).")
        print(f"{five_hundred_bill} five hundred bill(s).")
        print(f"{two_hundred_bill} two hundred bill(s).")
        print(f"{one_hundred_bill} one hundred bill(s).")

    else:
        print("Your money isn't enough to pay the cost.")


change(cost, money_given)
