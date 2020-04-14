# sum of the first n integers
# func(10) = 5050


def sum_of_integers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_integers(n-1)


if __name__ == '__main__':
    print(sum_of_integers(100))
    print(sum_of_integers(200))
    print(sum_of_integers(300))
