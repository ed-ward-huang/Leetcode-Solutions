"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        ## nested for loop, comparing each interval with all other intervals to see if they conflict
        ## O(n^2)
        if not intervals:
            return True
        
        newIntervals = []
        for i in intervals:
            newIntervals.append((i.start, i.end))
        

        heapq.heapify(newIntervals)

        while(newIntervals):
            curInterval = heapq.heappop(newIntervals)

            if newIntervals and curInterval[1] > newIntervals[0][0]:
                return False
        
        return True
        




