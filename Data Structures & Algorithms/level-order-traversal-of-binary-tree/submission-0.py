# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = {} #Level, nodeList
        def dfsLevel(cur, level):
            if not cur:
                return 
            
            if level not in hm:
                hm[level] = []
            hm[level].append(cur.val)

            dfsLevel(cur.left, level + 1)
            dfsLevel(cur.right, level + 1)

        dfsLevel(root, 0)

        return [v for k,v in hm.items()]