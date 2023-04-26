# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def bfs(root):
            visited=set([root])
            que=deque([root])
            
            result=[]
            
            
            
            while que:
                curr_len=len(que)
                total=0
                
                for _ in range(curr_len):
                    node=que.popleft()
                    total+=node.val
                    
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
                    
                result.append(total/curr_len)
            return result
                
        return bfs(root)

                
                    
                
            
            
            
            
        