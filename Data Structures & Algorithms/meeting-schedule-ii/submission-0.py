"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        ## given list of intervals (unsorted), find minimum number of days required to schedule all meetings without conflicts

        ## what if no meetings [] -> return 0?
        ## (0,8), (8,10) is not a conflict
        ## will there be a large number of intervals?

        ## (0,10) (5,15) (12,18) (16,20) -> 2
        ## (0,10) (5,18) (12,18) (16,20) -> 3
        ## (0,10) (2,10) (12,15) (13,20) -> 3

        ## (0,10) (5,15), (12,15) -> total days requried = 3

        ## know there is a conflict when nextStart < end
        ## sorted array of intervals
        ## endDays = []
        ## if there exists a endDay with no conflict, we would update our Enday of that one
        ## return len(endDays) 

        newIntervals = []
        for i in intervals:
            newIntervals.append((i.start, i.end))
        
        heapq.heapify(newIntervals) ## sorted now

        endDays = []
        while newIntervals:
            curInterval = heapq.heappop(newIntervals)

            inserted = False
            for i in range(len(endDays)):
                if endDays[i] <= curInterval[0]:
                    ## why do we not care which endDays is updated
                    ## say endDays = [6, 8, 10]
                    ## curInterval = [9, x] nextInterval = [>=9, y]
                    inserted = True
                    endDays[i] = curInterval[1]
                    break
            
            if not inserted:
                endDays.append(curInterval[1])
        
        return len(endDays)







