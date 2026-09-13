# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        def dfs(node):
            if not node:
                data.append("N")
                return
            
            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(data)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None 

        nodes = data.split(",")
        counter = 0

        def reverseDFS():
            nonlocal counter 

            if nodes[counter] == "N":
                counter += 1 
                return None 

            newNode = TreeNode(int(nodes[counter]))
            counter += 1 

            newNode.left = reverseDFS()
            newNode.right = reverseDFS()

            return newNode 
        
        return reverseDFS()
        
            


