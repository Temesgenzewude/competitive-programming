# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.tilts=0
        
        def helper(root):
            if not root:
                return 0
            leftSum=helper(root.left)
            rightSum=helper(root.right)
            
            
            
            self.tilts+=abs(rightSum-leftSum)
            
            return leftSum+rightSum + root.val
        
        helper(root)
        
        return self.tilts
    
    
            
            
            
            
            
            
        