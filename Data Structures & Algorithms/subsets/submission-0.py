class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        res = []

        def backtracking(index: int, sublist: List[int]):
            nonlocal res
            
            if index == len(nums):
                res.append(sublist[:])
                return
            
            ## option 1: add to sublist

            sublist.append(nums[index])
            backtracking(index + 1, sublist)


            sublist.pop()
            ## option 2: dont add to sublist
            backtracking(index + 1, sublist)
        
        backtracking(0, [])
        return res