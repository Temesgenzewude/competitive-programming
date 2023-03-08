# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.left=p.val if p.val < q.val else q.val
        self.right=q.val if q.val>p.val else p.val
        
        def helper(root):
            if not root:
                return
            if root.val >=self.left and root.val <=self.right:
                return root
            elif root.val > self.left and root.val > self.right:
                return helper(root.left)
            elif root.val < self.left and root.val < self.right:
                return helper(root.right)
            
            
        return helper(root)
                
            
            
            
        
        