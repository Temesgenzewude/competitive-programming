# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            helper(node.right)
            ans.append(node.val)
            
        helper(root)
        
        return ans
        
#         while root:
#             self.postorderTraversal(root.left)
#             self.postorderTraversal(roo.right)
#             return root.valfff

        