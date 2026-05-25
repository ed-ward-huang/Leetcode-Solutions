from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = [0] * 26

        for t in tasks:
            ## subtrack because we need a maxHeap
            counter[ord(t) - ord('A')] -= 1

        ## this is now a maxHeap where element from counter is actually = -element
        heapq.heapify(counter)
        waitList = deque([]) ## maxfrequency, time + n
        time = 0

        while counter or waitList:
            if counter:
                maxfrequency = heapq.heappop(counter) + 1
                if maxfrequency < 0:
                    waitList.append((maxfrequency, time + n))
            
            while counter and counter[0] >= 0:
                heapq.heappop(counter)

            while waitList and  waitList[0][1] == time:
                val, cooldown = waitList.popleft()
                heapq.heappush(counter, val)
            
            time += 1
        
        return time


