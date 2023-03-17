# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.result=[]
        
        
        def helper(root):
            queue= collections.deque()
            queue.append(root)
            
            while queue:
                n=len(queue)
                level=[]
                for i in range(n):
                    node=queue.popleft()
                    if node:
                        level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                if level:
                    self.result.append(level)
        
        
        helper(root)
 
        
        return self.result
            
            
            
            
            
            
            
        