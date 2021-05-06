def canAttendMeetings(intervals):
    n = len(intervals)
    intervals = sorted(intervals, key = lambda interval: interval[0])

    for i in range(n-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True

intervals = [[7,10],[2,4]]
res = canAttendMeetings(intervals)
print(res)

