# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths=[]
       
        
        
        def helper(root, path=[]):
            
            if not root.left and not root.right:
                paths.append("->".join(path))
                
                return
            
            if root.left:
                helper(root.left, path + [str(root.left.val)])
            if root.right:
                helper(root.right, path + [str(root.right.val)])
                
        helper(root,[str(root.val)] )
        
        return paths
           
            
            
            
            
            
                
                
                
                
            
            
        