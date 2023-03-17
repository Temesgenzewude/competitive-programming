# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        
        
        def helper(root):
           
            max_width=1
            currLevel=[(root,1)]
            
            while currLevel:
                nextLevel=[]
                
                for node, pos in currLevel:
                    if node.left:
                        nextLevel.append((node.left, pos*2))
                    if node.right:
                        nextLevel.append((node.right, pos*2 +1))
                if nextLevel:
                    max_width=max(max_width, nextLevel[-1][1]-nextLevel[0][1]+1)
                currLevel=nextLevel
            
            return max_width
       
        return helper(root)
       

            
        