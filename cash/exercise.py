def prompt_change():
    while True:

        change_owed = float(input("Change owed: "))

        if change_owed > 0:
            return change_owed


def calculate():
    change = prompt_change()
    coins = [0.25, 0.10, 0.05, 0.01]
    coin_count = 0

    for coin in coins:
        while change >= coin:
            change = round(change-coin, 2)
            coin_count += 1
            print(change)

    print(coin_count)


if __name__ == '__main__':
    calculate()
