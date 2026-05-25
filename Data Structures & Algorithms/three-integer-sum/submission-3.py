class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() ## O(nlogn)
        res = []

        for i, a in enumerate(nums):

            if a > 0: break

            if i > 0 and a == nums[i - 1]:
                continue

            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                if nums[lp] + nums[rp] + a == 0:
                    res.append([a, nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1

                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
                elif nums[lp] + nums[rp] + a > 0:
                    rp -= 1
                else:
                    lp += 1
        

        return res




