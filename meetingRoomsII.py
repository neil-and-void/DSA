'''
# idea: sort by start time, shove as many meetings into a single room until there is an overlap, then add another meeting room
def minMeetingRoomsII(intervals):
    minHeap = new MinHeap()
    insert 0 in minHeap

    sort the intervals by start time

    for each interval in intervals
        get meeting room with earliest end time (ie. the top element of heap)
        if interval starts after this time
            add interval to this meeting room (ie. replace the endtime of this meeting room with the endtime of interval)
        if interval starts before this time
            add interval to a new meeting room (ie. add endtime to heap)

    return size of heap
S: O(n) + O(k) | T: O(nlogn) + O(nlogk), k = size of heap
'''
import heapq

def minMeetingRoomsII(intervals):
    minHeap = [0]

    intervals = sorted(intervals, key = lambda interval: interval[0])


    for interval in intervals:
        minEndTime = minHeap[0]
        if minEndTime <= interval[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval[1])
        if interval[0] < minEndTime:
            heapq.heappush(minHeap, interval[1])

    return len(minHeap)

intervals = [[7,10],[2,4]]
res = minMeetingRoomsII(intervals)

