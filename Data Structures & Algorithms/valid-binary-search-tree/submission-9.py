# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lowLimit, highLimit):
            if not node:
                return True 
            
            if not (lowLimit < node.val < highLimit):
                return False 
            
            return dfs(node.left, lowLimit, node.val) and dfs(node.right, node.val, highLimit)

        return dfs(root, -float("inf"), float("inf"))

         
