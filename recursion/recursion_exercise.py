# Collatz conjecture
# If n is 1, stop.
# if n is even repeat this process on n/2
# if n is odd, repeat this process on 3n+1

# Calculate how many steps it takes to get to 1


def collatz(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        n = n/2
    else:
        n = (3*n)+1
    return collatz(n) + 1

