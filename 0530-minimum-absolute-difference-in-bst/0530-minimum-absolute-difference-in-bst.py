# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#         minDif=float('inf')
#         prevVal=None
        
#         def inorder(node):
            
#             nonlocal minDif
#             nonlocal prevVal
#             if not node:
#                 return 
            
#             inorder(node.left)
            
#             if prevVal:
#                 minDif=min(minDif, node.val-prevVal)
            
            
#             prevVal=node.val
            
            
#             inorder(node.right)
        
#         inorder(root)
        
#         return minDif

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        cur, stack, minDiff, prev = root, [], 10**5, -10**5
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            minDiff = min(minDiff, node.val - prev)
            prev = node.val
            cur = node.right
        
        return minDiff
    
        