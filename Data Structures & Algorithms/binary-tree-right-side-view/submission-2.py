# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def depthFirstSearch(node, depth):
            if not node:
                return
            
            if len(res) < depth:
                res.append(node.val)
            
            if node.right:
                depthFirstSearch(node.right, depth + 1)
            if node.left:
                depthFirstSearch(node.left, depth + 1)
        
        depthFirstSearch(root, 1)

        return res