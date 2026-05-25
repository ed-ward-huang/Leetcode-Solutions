# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        
        def validate(node, minValue, maxValue):
            if not node:
                return True
            
            ## check that node.val is within range
            if not(minValue < node.val < maxValue):
                return False
            

            return validate(node.left, minValue, node.val) and validate(node.right, node.val, maxValue)


        return validate(root, -2000, 2000)