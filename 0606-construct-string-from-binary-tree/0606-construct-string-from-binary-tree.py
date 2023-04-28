# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        result=[]
        
        def preorder(node):
            
            if not node:
                return
            
            result.append("(")
            
            result.append(str(node.val))
            if not node.left and node.right:
                result.append("()")
            
            preorder(node.left)
            preorder(node.right)
            
            result.append(")")
            
        
        preorder(root)
        
        return "".join(result)[1:-1]
            
            
            
            
            
        
        
        
        