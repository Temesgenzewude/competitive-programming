# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum=root.val
        
        
        def helper(root):
            if not root:
                return 0
            
            left=max(helper(root.left),0)
            right=max(helper(root.right),0)
            
            curr_max=root.val+left+right
            
            self.max_path_sum=max(self.max_path_sum,curr_max)
            
            
            return root.val + max(left, right)
        
        helper(root)
        
        return self.max_path_sum
            
        