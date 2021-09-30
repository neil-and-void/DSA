from typing import *
from collections import defaultdict
from queue import deque


def countComponents(n: int, edges: List[List[int]]) -> int:
    visited = [False] * n
    graph = dict()

    for v1, v2 in edges:
        if v1 not in graph:
            graph[v1] = [v2]
        else:
            graph[v1].append(v2)
        if v2 not in graph:
            graph[v2] = [v1]
        else:
            graph[v2].append(v1)

    queue = deque()
    count = 0

    for vertex in range(n):

        if not visited[vertex]:
            queue.append(vertex)

            # bfs
            while 0 < len(queue):
                # print(queue)
                curVertex = queue.popleft()
                visited[curVertex] = True
                # add children
                neighbors = graph.get(curVertex, [])
                for neighbor in neighbors:
                    if not visited[neighbor]:
                        queue.append(neighbor)

            count += 1
    return count


n = 5
edges = [[0,1],[1,2],[3,4]]

ans = countComponents(n, edges)
print(ans)




