"""
idea:


class MinStack:
    def __init__(self):
        self.stackList = []
        self.minList = []

    def top(self):
        pass

    def push(self, x):
        append to stack list

        if x is smaller than the top elemtn of the min list
            push x to the top of the min list since it is the new min
        else if x is >= the top element of the min list
            append the top of the min list to the min listj

    def pop(self, x):
        pop from both from stack list and min listj
        return popped from stack list

    def getMin(self):
        pop from both
        return poppped from getMin
"""

class MinStack:
    def __init__(self):
        self.stackList = []
        self.minList = []

    def top(self):
        return self.stackList[0]

    def push(self, x):
        self.stackList.append(x)

        if x < self.minList[-1]:
            self.minList.append(x)
        else if x >= self.minList[-1]:
            sefl.minList.append(self.minList[-1])

    def pop(self, x):
        self.stackList.pop()
        self.minList.pop()

    def getMin(self):
        return self.minList

