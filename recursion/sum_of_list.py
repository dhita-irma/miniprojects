# calculate the sum of a list of numbers


def sum_of_list(items):
    if len(items) == 0:
        return -1
    elif len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_of_list(items[1:])


if __name__ == '__main__':
    print(sum_of_list([2, 4, 5, 6, 7]))
    print(sum_of_list([3, 5, 7, 9, 11]))
    print(sum_of_list([2, 3, -5, -5]))
