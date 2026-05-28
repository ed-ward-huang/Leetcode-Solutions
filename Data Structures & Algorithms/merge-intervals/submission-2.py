class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ## sort by when they start
        intervals.sort(key = lambda x: x[0])

        ## intervals that start the earliest come first
        ## to know an interval overlaps: end1 >= start2
            ## if end1 < start2 < start3
        ## to merge we get start1, end2
        if not intervals:
            return []

        res = []

        for i in range(1, len(intervals)):
            if intervals[i - 1][1] >= intervals[i][0]:
                ## know we want to merge
                intervals[i] = [intervals[i - 1][0], max(intervals[i][1], intervals[i - 1][1])]
            else:
                res.append(intervals[i - 1])
        
        res.append(intervals[-1])
        return res

