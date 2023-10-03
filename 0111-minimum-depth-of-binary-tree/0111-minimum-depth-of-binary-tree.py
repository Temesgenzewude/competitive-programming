# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            left, right= dfs(root.left), dfs(root.right)
            
           
            
            
            return 1+min(left, right)
        
        
        if not root:
            return 0
    
        self.min_depth=float('inf')

        self.dfs(root, 0)

        return self.min_depth
        
        
        
    
    def dfs(self, root, curr_depth):
        
        if not root:
            return
        
        if not root.left and not root.right:
            self.min_depth= min(self.min_depth, curr_depth+1)
        
        self.dfs(root.left, curr_depth+1)
        self.dfs(root.right, curr_depth+1)
        
    
    
        
            
            
        