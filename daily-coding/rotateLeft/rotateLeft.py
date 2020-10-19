def rotateLeft(d, arr):
    for i in range(0, d):
        arr.append(arr[0])
        arr.remove(arr[0])
    return arr


if __name__ == "__main__":
    rotateLeft(5, [1, 2, 3, 4, 5])
