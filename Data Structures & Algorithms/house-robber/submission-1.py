class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def findHouses(index):
            if index >= len(nums):
                return 0
            
            if index in memo:
                return memo[index]
            
            maxAtIndex = max(findHouses(index + 1), nums[index] + findHouses(index + 2))
            memo[index] = maxAtIndex
            
            return maxAtIndex
    
        return findHouses(0)
