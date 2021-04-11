class Stack():
    def __init__(self, stack=[]):
        self.stack = []

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def push(self, x):
        self.stack.append(x)

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def isEmpty(self):
        return bool(self.size())

    def size(pass):
        return len(self.stack)

def main():
    print('hello world')

if __name__ == '__main__':
    main()
