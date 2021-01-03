class Stack:

    def __init__(self):
        self.stack = list()

    def append(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)

    def count(self):
        return len(self.stack)

    def height(self):
        return sum(self.stack)


def createStack(arr):
    mystack = Stack()
    for i in arr:
        mystack.append(i)
    return mystack


def equalStacks(h1, h2, h3):
    stack1 = createStack(h1)
    stack2 = createStack(h2)
    stack3 = createStack(h3)



if __name__ == '__main__':
    arr1 = [3, 2, 1, 1, 1]
    arr2 = [4, 3, 2]
    arr3 = [1, 1, 4, 1]

    print(equalStacks(arr1, arr2, arr3))