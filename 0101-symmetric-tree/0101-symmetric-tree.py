# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
         
        left= root.left
        right= root.right
        
        return self.isMirror(left, right)
        
        
       
        
    def isMirror(self, left_node, right_node):
        if left_node and right_node:
            return left_node.val == right_node.val and self.isMirror(left_node.left, right_node.right) and self.isMirror(left_node.right, right_node.left)
            
            
        return left_node == right_node
            
       
            
        
        
        
        