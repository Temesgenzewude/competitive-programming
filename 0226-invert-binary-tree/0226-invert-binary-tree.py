# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is None:
            return None
        
        rightSide=self.invertTree(root.right)
        leftSide=self.invertTree(root.left)
        
        root.right=leftSide
        root.left=rightSide
        
        return root
        