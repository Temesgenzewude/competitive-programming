# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prevVal = -float("inf")
        
        def isValid(node):
          
            if not node:
                return True
            
            left_truth= isValid(node.left)
            if self.prevVal < node.val:
                self.prevVal=node.val
            else:
                return False
            
            right_truth= isValid(node.right)
            
            return left_truth and right_truth
            
            
        
        return isValid(root)
        
        
#         if len(result)<=1:
#             return True
#         for i in range(1, len(result)):
#             if result[i] <= result[i-1]:
#                 return False
        
#         return True
        
        
        
#             if not node:
#                 return True
#             if node.left and node.val <= node.left.val:
#                 return False
#             elif node.right and node.val >= node.right.val:
#                 return False
            
            
            
#             return isValid(node.left) and isValid(node.right)
        
        
#         return isValid(root)
        
            
            
        