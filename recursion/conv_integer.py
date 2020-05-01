def to_string(n, base):
    str_num = "0123456789ABCDEF"

    if n < base:
        return str_num[n]
    else:
        return to_string(n//base, base) + str_num[n % base]


if __name__ == '__main__':
    print(to_string(28, 10))
    print(to_string(10, 2))