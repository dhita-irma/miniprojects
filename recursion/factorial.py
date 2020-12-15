def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def main():
    n = input("Enter a number: ")
    print(f"Factorial of {n} is {str(factorial(int(n)))}")


if __name__ == '__main__':
    main()
