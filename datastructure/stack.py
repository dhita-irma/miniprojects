
class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, item):
        """Append an item to the end of the stack"""
        self.stack.append(item)

    def pop(self):
        """Remove the last item of the stack and return the value"""
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        """Get the value of the last item of the stack"""
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def clear(self):
        """Empty the stack"""
        if len(self.stack) > 0:
            self.stack.clear()
        else:
            return None

    def __str__(self):
        """Print all the items in the stack"""
        return str(self.stack)

    def count(self):
        return len(self.stack)
