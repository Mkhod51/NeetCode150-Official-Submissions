# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        ret = None 
        
        def dfs(node):
            nonlocal count 
            nonlocal ret 

            if ret:
                return
            if not node:
                return 
            
            
            dfs(node.left)

            if count == k:
                ret = node.val 
            count += 1 

            dfs(node.right)
        
        dfs(root)    
        return ret 