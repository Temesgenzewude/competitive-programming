# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(root):
            if not root:
                return TreeNode(val)
            if val<root.val:
                root.left=insert(root.left)
            elif val>root.val:
                root.right=insert(root.right)
            
            return root
        return insert(root)
            
            
            
#             if val > node.val:
#                 return True
#             else:
#                 return False
        
#         node=root
        
#         while node.left or node.right:
            
#             if isGreater(node):
#                 node= node.right
#             else:
#                 node=node.left
        
#         if not node.left:
#             node.left=TreeNode(val)
#         elif not node.right:
#             node.right=TreeNode(val)
        
                
       


                

        
        
        
            
            
        