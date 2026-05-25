class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxWater = 0
        while l < r:
            ## calculate water
            water = min(heights[l], heights[r]) * (r - l)
            maxWater = max(maxWater, water)

            if heights[l] == heights[r]:
                l += 1
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater
