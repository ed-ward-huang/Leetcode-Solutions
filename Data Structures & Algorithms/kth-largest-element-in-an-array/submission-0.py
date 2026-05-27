class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ## .sort(), search from back, O(nlogn)

        for n in range(len(nums)):
            nums[n] *= -1
        
        heapq.heapify(nums)
        
        count = 0
        while nums and count < k:
            current = heapq.heappop(nums) * -1 
            count += 1

        return current