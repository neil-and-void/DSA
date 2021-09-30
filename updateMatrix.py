from collections import deque
from typing import *

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    ans = [[10001 for i in range(len(mat[0]))] for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                ans[i][j] = min(bfs(mat, i,j), ans[i][j])
            else:
                ans[i][j] = 0
    print(ans)

def bfs(mat, i, j):
    visited = [[False for i in range(len(mat[0]))] for i in range(len(mat))]
    parents = dict()
    queue = deque()

    queue.append((i,j))
    while len(queue):
        cur_i, cur_j = queue.popleft()
        visited[cur_i][cur_j] = True

        if mat[cur_i][cur_j] == 0:
            count = 0
            cur_pair = (cur_i, cur_j)
            while cur_pair[0] != i or cur_pair[1] != j:
                print(parents)
                cur_pair = parents[cur_pair]
                count += 1
            return count

        # up 
        if 0 <= cur_i - 1 and not visited[cur_i-1][cur_j]:
            parents[(cur_i-1, cur_j)] = (cur_i, cur_j)
            queue.append((cur_i-1, cur_j))
        # down
        if cur_i + 1 < len(mat)  and not visited[cur_i+1][cur_j]:
            parents[(cur_i+1, cur_j)] = (cur_i+1, cur_j)
            queue.append((cur_i + 1, cur_j))
        # left 
        if 0 <= cur_j - 1 and not visited[cur_i][cur_j - 1]:
            parents[(cur_i, cur_j-1)] = (cur_i, cur_j-1)
            queue.append((cur_i, cur_j - 1))
        # right 
        if cur_j + 1 < len(mat[0]) and not visited[cur_i][cur_j + 1]:
            parents[(cur_i, cur_j+1)] = (cur_i, cur_j+1)
            queue.append((cur_i, cur_j + 1))

mat = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
ans = updateMatrix(mat)
print(ans)

