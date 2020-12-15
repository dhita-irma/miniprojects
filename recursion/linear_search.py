# Recursive Linear Search Algorithm


def search(x, item_list):
    if x == item_list[0]:
        return 1
    else:
        return 1 + search(x, item_list[1:])


if __name__ == '__main__':

    my_list = [1, 3, 6, 5, 10, 8]
    for i in my_list:
        print(search(i, my_list))
