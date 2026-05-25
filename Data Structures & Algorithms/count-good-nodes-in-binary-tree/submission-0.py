# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        goodNodeCount = 0

        def bfs(node, maxValOnPath):
            nonlocal goodNodeCount

            if not node:
                return None

            if node.val >= maxValOnPath:
                goodNodeCount += 1

            bfs(node.left, max(maxValOnPath, node.val))
            bfs(node.right, max(maxValOnPath, node.val))
        

        bfs(root, -200)

        return goodNodeCount


