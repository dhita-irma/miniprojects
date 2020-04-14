def fibonacci(n):
    if n <= 0:
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    for i in range(1, 21):
        print(f"n = {i} -> {fibonacci(i)}")
