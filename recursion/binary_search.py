# Recursive Binary Search Algorithm


def search(x, item_list):
    mid_index = len(item_list) // 2
    if x == item_list[mid_index]:
        return mid_index
    elif x < item_list[mid_index]:
        return search(x, item_list[:mid_index])
    else:
        return 1 + mid_index + search(x, item_list[mid_index+1:])


if __name__ == '__main__':

    my_list = [0, 10, 20, 30, 40, 50, 60]
    for i in my_list:
        print(search(i, my_list))
