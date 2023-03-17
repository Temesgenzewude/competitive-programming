# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.count=0
        
        def helper(root):
            
            if not root:
                return [0,0]
            leftResult=helper(root.left)
            rightResult=helper(root.right)
          
            totalSum=leftResult[0] + rightResult[0]+ root.val
            totalNodes=leftResult[1]+rightResult[1]+1
            
            if totalSum//totalNodes==root.val:
                self.count+=1
            
            return [totalSum, totalNodes]
        
        helper(root)
        
        return self.count
            
        