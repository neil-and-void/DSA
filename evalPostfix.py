"""

def evalPostfix(tokens):
    stack= Stack()

    for t in tokens
        if t is a number
            push to stack
        if t is an operator
            pop 2 from the stack
            and apply operation
            push result back onto stack
    return pop from stack which should be the overall expression

"""


def evalPostfix(tokens):
    stack = []

    operations = {
        '*': lambda a, b: a * b,
        '/': lambda a, b : int(a / b),
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b
    }

    for t in tokens:
        try:
            stack.append(int(t))
        except ValueError:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operations[t](operand1, operand2)
            stack.append(result)
    return stack.pop()


def main():
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = evalPostfix(tokens)
    print(result)

if __name__ == '__main__':
    main()

