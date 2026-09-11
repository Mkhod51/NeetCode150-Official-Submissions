# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Stores node: level
        #for p and q, find them and add all their things to a set 
        #Find common ones
        #Return common one with greatest level 

        def findNode(root, node, soFar):
            soFar.append(root)

            if root is node:
                return soFar
            if node.val < root.val: 
                return findNode(root.left, node, soFar)
            else:
                return findNode(root.right, node, soFar)
            
        #finding p
        pNodes = findNode(root, p, [])
        qNodes = set(findNode(root, q, []))

        print(n.val for n in pNodes)
        print(n.val for n in qNodes)

        found = False
        while not found:
            curNode = pNodes.pop()

            if curNode in qNodes:
                found = True 
        
        return curNode


