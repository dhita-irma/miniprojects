# sum of digit


def sum_digit(n):
    str_n = str(n)
    if len(str_n) == 1:
        return int(str_n[-1])
    else:
        return int(str_n[-1]) + sum_digit(str_n[:-1])


if __name__ == '__main__':
    print(sum_digit(345))
    print(sum_digit(45))
    print(sum_digit(285))
