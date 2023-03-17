# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        prefix_count={0:1}
        self.currSum=0
        self.count=0
        self.prevVal=0
        
        
        def helper(root):
            
            if not root:                    
                return
            

            self.currSum+=root.val
            self.count+=prefix_count.get(self.currSum-targetSum,0)
            
            prefix_count[self.currSum]=1+prefix_count.get(self.currSum,0)
            
            helper(root.left)
            helper(root.right)
            
            prefix_count[self.currSum]-= 1
            
            self.currSum-=root.val
            
        
        helper(root)
        return self.count
            
                
                
            
            
        
        
        
        
        
        