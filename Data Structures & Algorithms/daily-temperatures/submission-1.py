class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## in this stack: (temp, day from start)
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) -1, -1, -1):
            ## stack is non empty
            query = (temperatures[i], i)
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1][1] - i
            
            stack.append(query)
        
        return res