"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

[]
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key= lambda x: x.start)

        timeOfLastMeeting = []
        heapq.heapify(timeOfLastMeeting)

        for i in intervals:
            start, end = i.start, i.end

            if timeOfLastMeeting and timeOfLastMeeting[0] <= start:
                heapq.heappop(timeOfLastMeeting)
                heapq.heappush(timeOfLastMeeting, end)
            else:
                heapq.heappush(timeOfLastMeeting, end)
        
        return len(timeOfLastMeeting)


