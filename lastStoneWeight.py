from DS.maxHeap import MaxHeap
"""
def lastStoneWeight(stones):
    for stone in stones
        add to max heap

    while heap has more than 1 stones
        take 2 stones from heap
        break together
        put the leftover back in
    return either stones[0] or 0
"""

def lastStoneWeight(stones):
    maxHeap = MaxHeap()

    for stone in stones:
        maxHeap.insert(stone)

    while len(maxHeap.heap) > 1:
        rock1 = maxHeap.pop()
        rock2 = maxHeap.pop()

        leftover = abs(rock1 - rock2)
        if leftover:
            maxHeap.insert(leftover)
    print(maxHeap.heap)


stones = [2,7,4,1,8,1] # 1 
lastStoneWeight(stones)
stones = [7,6,7,6,9] # 3
lastStoneWeight(stones)

