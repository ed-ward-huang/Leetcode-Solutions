
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        '''
        say we have 8, 5, 11, 9, 13
        at 8, we have assembed monostack = [13, 11, 5]

        ## so we would want a monotonic stack, keeping a decreasing list of values, popping out when we see them
        ## to see number of people can be viewed, go through monotonic stack until larger person appears than current person

        ## count number of people smaller than it + 1 if larger person exists


        Time Complexity: O(n) linear
        Space Complexity: O(n) linear
        '''

        monostack = []
        res = []
        for i in range(len(heights) -1, -1, -1):

            count = 0
            while monostack:
                if monostack[-1] > heights[i]:
                    count += 1
                    break
                else:
                    monostack.pop()
                    count += 1
            
            res.append(count)
            monostack.append(heights[i])

        res.reverse()
        return res

