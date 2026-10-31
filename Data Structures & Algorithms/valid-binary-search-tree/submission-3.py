# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#left subchild less than node 
#Right subchild more than node 

"""
   4
3
  5

  We might need to use some kind of minimum and maximum limits
  The max for a node is its parent if the parent is bigger, and the min is the parent if the parent is smaller 
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, minLim, maxLim):
            if not node:
                return True 
            if node.val >= maxLim or node.val <= minLim:
                return False 
            
            return dfs(node.left, minLim, node.val) and dfs(node.right, node.val, maxLim)

        return dfs(root, -float("inf"), float("inf"))
