from datastructure.stack import Stack

rStack = Stack()


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convert_string[n])
        else:
            rStack.push(convert_string[n % base])
        n = n // base
    result = ""
    while not rStack.is_empty():
        result = result + str(rStack.pop())
    return result


if __name__ == '__main__':

    print(to_str(1453, 16))
    print(to_str(10, 2))