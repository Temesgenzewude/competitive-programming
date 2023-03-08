# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        result=[]
        
        def isValid(node):
            if not node:
                return 
            
            isValid(node.left)
            result.append(node.val)
            isValid(node.right)
            
            
        
        isValid(root)
        if len(result)<=1:
            return True
        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return False
        
        return True
        
        
        
#             if not node:
#                 return True
#             if node.left and node.val <= node.left.val:
#                 return False
#             elif node.right and node.val >= node.right.val:
#                 return False
            
            
            
#             return isValid(node.left) and isValid(node.right)
        
        
#         return isValid(root)
        
            
            
        