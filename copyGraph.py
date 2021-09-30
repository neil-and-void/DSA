class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def copyGraph(node):
    copyGraphRec

def copyGraphRec(node, prevNode):
    newNode = Node(node.val)
    node.val *= -1

    for neighbor in node.neighbors:
        if 1 <= neighbor.val:
            newNeighbor = copyGraph(neighbor, newNode)
            newNode.neighbors.append(newNeighbor)
    newNode.neighbors.append(prevNode)
    return newNode

