# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        node_count={}
        result=[]
        
        def helper(root):
            if not root:
                return 
            helper(root.left)
            node_count[root.val]=1+node_count.get(root.val, 0)
            helper(root.right)
            
        helper(root)
            
        
        sorted_count=sorted(node_count.items(), key=lambda x: x[1], reverse=True)
        
        mode=sorted_count[0][1]
        result.append(sorted_count[0][0])
        
        for i in range(1,len(sorted_count)):
            if sorted_count[i][1]==mode:
                result.append(sorted_count[i][0])
                
            elif sorted_count[i][1]<mode:
                break
        
        return result
        
        
    
            
        