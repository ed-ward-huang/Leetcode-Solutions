class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:  
        
        res = []

        def findAllCombinations(curIndex: int, runningSum: int, currentNumbers:List[int]):
            nonlocal res
            ## exceed the target: return (adding any more numbers is waste of time)

            ## meet the target: append to res, return (since adding more nubmers is a waste of time)
            if runningSum == target:
                res.append(currentNumbers[:])
                return

            if runningSum > target or curIndex == len(nums):
                return
            
            ## make 2 choices
            currentNumbers.append(nums[curIndex])
            findAllCombinations(curIndex, runningSum + nums[curIndex], currentNumbers)

            currentNumbers.pop()
            findAllCombinations(curIndex + 1, runningSum, currentNumbers)

        findAllCombinations(0, 0, [])
        return res