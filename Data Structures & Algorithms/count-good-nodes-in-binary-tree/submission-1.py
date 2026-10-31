# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0 
        def dfs(node, maxSeen):
            nonlocal counter 

            if not node:
                return 
            
            if node.val >= maxSeen:
                counter += 1
                maxSeen = node.val 
            
            dfs(node.left, maxSeen)
            dfs(node.right, maxSeen)

        dfs(root, -float("inf"))

        return counter 
            