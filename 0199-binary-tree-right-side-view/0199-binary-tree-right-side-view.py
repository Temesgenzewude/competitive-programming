# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result=[root.val] if root else []
        
        
        
        
        def helper(root):
            currLevel=[root]
            
        
            while currLevel:
                nextLevel=[]

                for node in currLevel:
                    if node and node.left:
                        nextLevel.append(node.left)
                    if node and node.right:
                        nextLevel.append(node.right)
                if nextLevel:
                    result.append(nextLevel[-1].val)
                currLevel=nextLevel
                
        helper(root)
        
        return result
        
        
                
        
        
        
        
        
        
        