def reverse(lst):
    if len(lst) == 1:
        return lst
    else:
        return [lst[-1]] + reverse(lst[:-1])


print(reverse([1, 2, 3, 4, 5]))