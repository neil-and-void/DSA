def maxArea1(height):
    n = len(height)

    globalMax = 0
    runningWidth = 1
    runningMinHeight = float('inf')

    for i in range(1, n):
        cur = 0
        if min(height[i-1], height[i]) < min(height[i], runningMinHeight) * runningWidth:
            runningWidth = 1
            runningMinHeight = min(height[i-1], height[i])
        else:
            runningWidth += 1
            runningMinHeight = min(runningMinHeight, height[i])
        globalMax = max(globalMax, runningWidth * runningMinHeight)

    return globalMax

def maxArea(height):
    i = 0
    j = len(height) - 1
    curMax = 0

    while i < j:
        curMax = max(curMax, (j - i) * min(height[i], height[j]))
        print(curMax, j - i)
        if height[i] <= height[j]:
            i += 1
        else:
            j -=1
    return curMax
height = [2,3,4,5,18,17,6]
ans = maxArea(height)
print(ans)

