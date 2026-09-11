# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        levels = {}
        
        def dfsLevel(node, level):
            if not node:
                return 
            
            if level not in levels:
                levels[level] = []
            
            levels[level].append(node.val)
            dfsLevel(node.right, level + 1)
            dfsLevel(node.left, level + 1)
        
        dfsLevel(root, 0)

        return [v[0] for k,v in levels.items()]

            
        
        

        return ret 