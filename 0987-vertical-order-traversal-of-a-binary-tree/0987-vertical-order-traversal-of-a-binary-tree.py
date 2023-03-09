# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def helper(root, row, col, values_col):
            if not root:
                return
            if col in values_col:
                values_col[col].append((row, root.val))
            else:
                values_col[col]=[(row, root.val)]
            
            helper(root.left, row +1, col-1, values_col)
            helper(root.right, row +1, col+1, values_col)
            
        
        row=col=0
        values_col={}
        result=[]
        
        helper(root, row,col,values_col)
        
        for key in sorted(values_col.keys()):
            temp=[column[1] for column in sorted(values_col[key])]
            result.append(temp)
        
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        