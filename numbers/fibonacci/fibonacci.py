n = int(input("Enter a number "))


def fibonacci(n):
    a = 0
    b = 1
    for x in range(n):
        yield a + b
        a, b = b, a+b


sequence = [num for num in fibonacci(n)]
print(sequence)
