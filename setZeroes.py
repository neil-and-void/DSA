'''
observations:
    - if we want to have O(1) space, we must use the matrix itself to store info
    - changing rows and cols to 0 interferes with itself since 0 is an indicator to change
        row and col, must store info and then act on it after collecting info

idea: iterate and set rows and cols to 0
    - can't work because of interference

idea:
    - iterate over the matrix and mark the row and col with inf
    - keep track if row and col have 0
    - go over colIndicator and rowIndicator and change rows and cols to 0's
    - if [0][0] change both row and col indicators to 0's
    - if one or the other, then change that one
'''
def setZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = float('inf')
                matrix[0][j] = float('inf')

    firstColZero = False
    firstRowZero = False

    for i in range(1, n):
        if matrix[i][0] == 0:
            firstColZero = True
            matrix[i][0] = float('inf')
        if matrix[i][0] == float('inf'):
            for j in range(m):
                matrix[i][j] = 0

    for j in range(1, m):
        if matrix[0][j] == 0:
            firstRowZero = True
            matrix[0][j] = float('inf')
        if matrix[0][j] == float('inf'):
            for i in range(n):
                matrix[i][j] = 0
    print(firstColZero, firstRowZero)
    if matrix[0][0] == 0 or (firstColZero and firstRowZero):
        # first row and col to 0
        for i in range(n):
            matrix[i][0] = 0
        for j in range(m):
            matrix[0][j] = 0
    elif firstColZero:
        for i in range(n):
            matrix[i][0] = 0
    elif firstRowZero:
        for j in range(m):
            matrix[0][j] = 0



m =[
    [-4,-2147483648,6,-7,0],
    [-8,6,-8,-6,0],
    [2147483647,2,-9,-6,-10]
]

ans = setZeroes(m)

for row in m:
    print(row)

