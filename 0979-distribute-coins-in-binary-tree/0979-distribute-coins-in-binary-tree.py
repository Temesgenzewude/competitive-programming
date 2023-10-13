# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.moves=0
        
        def dfs(root):
            
            if not root:
                return 0
            
            if not root.left and not root.right:
                self.moves+=abs(root.val-1)
                return root.val-1
            
            left= dfs(root.left)
            right=dfs(root.right)
            self.moves+=abs(left+right+root.val-1)
            
            return left+right+root.val-1
        
        dfs(root)
        
        
        return self.moves
        
    
        
        
        
        
        
        
        
        
        
        