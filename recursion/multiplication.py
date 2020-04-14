# Give a recursive algorithm for computing nx whenever n
# is a positive integer and x is an integer, using just addition.


def multiplication(n, x):
    if n <= 0:
        return -1
    if n == 1:
        return x
    else:
        return x + multiplication(n-1, x)


if __name__ == '__main__':
    for n in range(1, 11):
        print(f"{n}*5 = {multiplication(n, 5)}")
