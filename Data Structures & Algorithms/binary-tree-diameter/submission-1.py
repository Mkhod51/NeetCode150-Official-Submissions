# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0 

        def getDiam(node):
            nonlocal best 

            if not node:
                return 0
            left = getDiam(node.left)
            right = getDiam(node.right )
            res = 1 + max(left,right)
            best = max(best, left + right)
            return res
        
        getDiam(root)
        return best 
        

