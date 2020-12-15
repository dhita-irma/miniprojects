# Smallest number of coins needed for a change

def min_change(coin_list, change, known_result):
    min_coins = change
    if change in coin_list:
        known_result[change] = 1
        return 1
    elif known_result[change] > 0:
        return known_result[change]
    else:
        for i in [coin for coin in coin_list if coin <= change]:
            num_coins = 1 + min_change(coin_list, change-i, known_result)
            if num_coins < min_coins:
                min_coins = num_coins
                known_result[change] = min_coins
    return min_coins


print(min_change([1, 5, 10, 25], 63, [0]*64))
