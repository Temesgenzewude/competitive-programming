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
        
        
       
        
    def isMirror(self, lft_rt, rgt_rt):
        if lft_rt and rgt_rt:
            return lft_rt.val == rgt_rt.val and self.isMirror(lft_rt.left, rgt_rt.right) and self.isMirror(lft_rt.right, rgt_rt.left)
            
            
        return lft_rt == rgt_rt
            
       
            
        
        
        
        