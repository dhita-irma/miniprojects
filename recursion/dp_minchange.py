def dp_change(coin_list, change, min_coins, coin_used):
    for cents in range(change+1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_list if c <= cents]:
            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents-j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coin_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin


def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coins_used = [0] * (amnt+1)
    coins_count = [0] * (amnt+1)

    print("Making change for ", amnt, "requires")
    print(dp_change(clist, amnt, coins_count, coins_used), "coins")
    print("They are:")
    print_coins(coins_used, amnt)
    print(coins_used)


if __name__ == '__main__':
    main()
