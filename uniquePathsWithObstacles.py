'''
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    # base
    if current cell is bottom right of grid:
        add 1 to answer

    if current cell is outside of the grid
        return 0

    # recursive
    down = uniquePathsWithObstacles(down)
    right = uniquePathsWithObstacles(right)

    return down + right

'''
'''
#idea: brute force with backtracking
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    memo = {}
    return uniquePathsWithObstaclesRec(obstacleGrid, 0, 0, memo)

def uniquePathsWithObstaclesRec(grid, i, j, memo):
    if (i, j) in memo:
        return memo[(i, j)]
    m = len(grid)
    n = len(grid[0])

    # base
    if i == m - 1 and j == n - 1:
        return 1

    if i >= m or j >= n:
        return 0

    if grid[i][j] == 1:
        return 0

    # recursive
    right = uniquePathsWithObstaclesRec(grid, i+1, j, memo)
    down = uniquePathsWithObstaclesRec(grid, i, j+1, memo)

    if (i, j) not in memo:
        memo[(i, j)] = down + right

    return down + right
'''
from typing import *


'''
learned:
    - when identifying backtracking problem, always see if we have sub optimal or overlapping substructure properties
      because it might mean that this is a DP problem
    - pattern can be used here by seperating the iterative and base case in the innermost loop and differentiating
      separating them by the if statement for the base case
idea:
def uniquePathsWithObstacles(obstacleGrid):
    since we have a table made for us, no need to make one

    start at bottom right

    for i from m - 1 to 0
        for j from n - 1 to 0
            down = 0
            if down is not outside of grid:
                down = numPaths of down
            right = 0
            if right is not outside of grid:
                right = numPaths of right
            if cell at [i,j] is not blocked (ie, not equal to 1)
                cell = down + right
            else:
                cell = 0
'''
def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            # base
            if i == m - 1 and j == n - 1:
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = 1

            # iterative (same as recursive case)
            else:
                down = 0
                if i + 1 < m:
                    down = obstacleGrid[i+1][j]
                right = 0
                if j + 1 < n:
                    right = obstacleGrid[i][j+1]

                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = down + right

                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0

    return obstacleGrid[0][0]

grid = [[0,0,0],[0,1,0],[0,0,0]]
res = uniquePathsWithObstacles(grid)
print(grid)
print(res)

