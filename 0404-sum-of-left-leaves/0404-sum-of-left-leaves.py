# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # Define a helper function to recursively traverse the tree and compute the sum of left leaves
        def traverse(node, is_left):
            # If the current node is None, return 0
            if not node:
                return 0
            
            # If the current node is a leaf node and is a left child, return its value
            if not node.left and not node.right and is_left:
                return node.val
            
            # Recursively traverse the left and right subtrees
            left_sum = traverse(node.left, True)
            right_sum = traverse(node.right, False)
            
            return left_sum + right_sum
        
        # Call the helper function with the root node and False to indicate that the root is not a left child
        return traverse(root, False)
        