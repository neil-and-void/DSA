'''
idea:
 - add everything into a max heap
 - when popping, only increase count when we encounter a different number

def findKthLargest(nums, k):
    heapify nums into min heap

    pop until seen k distinct elements or different
    return that kth element
'''
import heapq

def findKthLargest(nums, k):
    maxHeap = []
    for num in nums:
        heapq.heappush(maxHeap, -num)

    while k > 0:
        cur = heapq.heappop(maxHeap)
        k -= 1

    return cur * -1

nums = [3,2,1,5,6,4]
k = 2
ans = findKthLargest(nums, k)
print(ans)

