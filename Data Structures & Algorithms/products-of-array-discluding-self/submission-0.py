class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        ## pass, go from left to right, keeping aggregating total and multiply to res
        runningProduct = 1
        for i in range(len(nums)):
            res[i] *= runningProduct
            runningProduct *= nums[i]

        ## same thing as above but from right to left
        runningProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= runningProduct
            runningProduct *= nums[i]
        
        return res
