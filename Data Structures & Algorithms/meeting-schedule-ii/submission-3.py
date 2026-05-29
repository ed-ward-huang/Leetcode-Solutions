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

        for i in intervals:
            start, end = i.start, i.end
            meetingAdded = False

            for t in range(len(timeOfLastMeeting)):
                if timeOfLastMeeting[t] <= start:
                    meetingAdded = True
                    timeOfLastMeeting[t] = end
                    break
            
            if not meetingAdded:
                timeOfLastMeeting.append(end)
        
        return len(timeOfLastMeeting)


