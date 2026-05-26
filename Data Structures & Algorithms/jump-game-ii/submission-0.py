class Solution:
    def jump(self, nums: List[int]) -> int:
        
        totalJumps = 0
        def recursiveJumpStep(curIndex):
            nonlocal totalJumps

            if curIndex == len(nums) - 1:
                return
            
            if curIndex + nums[curIndex] + 1 >= len(nums):
                totalJumps += 1
                recursiveJumpStep(len(nums) - 1)
                return

            bestMoveIndex = -1
            bestMoveDistance = -1

            for i in range(curIndex + 1, curIndex + nums[curIndex] + 1):
                if (i - curIndex) + nums[i] > bestMoveDistance:
                    bestMoveDistance = (i - curIndex) + nums[i]
                    bestMoveIndex = i
            
            totalJumps += 1
            recursiveJumpStep(bestMoveIndex)
        
        recursiveJumpStep(0)
        return totalJumps



            
