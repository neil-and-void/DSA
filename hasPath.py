'''
idea: dfs until hit wall, then go to available directions, making sure to mark our trail

- cannot go back from the direction it came from
def hasPath( maze: List[List[int]], start: List[int], destination: List[int], direction) -> bool:
    if hit wall (ie, ball has stopped)
        ### base ###
        
        #success
        if curCell is the destination
            done, return true

        recurse in each direction

    else
        ### recursive ###

        #backtrack
        if direction of cell is parallel to current direction
            stop, return

        # keep going (ie recurse) if:
        if current cell is new (ie 0)
            if current cell has been visited but is perpendicular to direction 

        mark current cell with what ever the direction is
        carry on (ie recurse) in direction
'''
from typing import *
from enum import Enum

def hasPath( maze: List[List[int]], start: List[int], destination: List[int]) -> bool: 
    class Direction(Enum):
        UP = 2
        DOWN = 4
        LEFT = 3
        RIGHT = 5

    def hasPathDFS(maze, start, destination, i, j, direction):
        # hit wall
        n = len(maze)
        m = len(maze[0])
        if :
            pass
            if i == destination[0] and j == destination[1]:
                wqa return True

            return (hasPathDFS(maze, start, destination, i-1, j, Direction.UP)
            or hasPathDFS(maze, start, destination, i+1, j, Direction.DOWN)
            or hasPathDFS(maze, start, destination, i, j-1, Direction.LEFT)
            or hasPathDFS(maze, start, destination, i, j+1, Direction.RIGHT))
        # path

    return hasPathDFS(maze, start, destination, 0,0,3)
         

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
ans = hasPath(maze, start, destination)
print(ans)

