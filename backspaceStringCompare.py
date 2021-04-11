"""
def backspaceStringCompare(T, S):
    create 2 stacks

    for character in T:
        if character is hashtag:
            pop from stack
        else:
            push onto stack

    for character in S
        if character is hashtag:
            pop from stack
        else:
            push onto stack

    return if both stacks are the same

    space: o(n * m)
    time: o(n + m)

"""


def backspaceStringCompare(T, S):
    print(T,S)

def main():
    S = "ab#c"
    T = "ad#c"
    result = backspaceStringCompare(T,S)
    print(result)

if __name__ == '__main__':
    main()

