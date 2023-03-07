# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        cur=root
        stack=[]
        ans=[]
        
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            ans.append(node.val)
            helper(node.right)
        helper(root)
        
        return ans
    
        
            
        
        
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur=cur.left
        #     cur= stack.pop()
        #     output.append(cur.val)
        #     cur=cur.right
        # return output
        
        
#         def inorder(root):
      
#             if root:
#                 inorder(root.left)
#                 output.append(root.val)
#                 inorder(root.right)
                
#         inorder(root)
        
        
        
        
#         return output

        