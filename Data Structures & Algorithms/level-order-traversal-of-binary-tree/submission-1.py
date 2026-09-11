# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        

        ret = []
        q = deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                curNode = q.popleft()
                level.append(curNode.val)

                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            
            ret.append(level)
        
        return ret



