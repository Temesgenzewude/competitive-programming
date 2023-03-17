# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        sum_count={}
        result=[]
        
        def helper(root):
            if not root:
                return 0
            left=helper(root.left)
            right=helper(root.right)
            
            sub_sum=left+right+root.val
            sum_count[sub_sum]=1+sum_count.get(sub_sum,0)
            
            return sub_sum
        
        helper(root)
        
        sorted_sum_count=sorted(sum_count.items(), key=lambda x: x[1], reverse=True)
        most_frq=sorted_sum_count[0][1]
        result.append(sorted_sum_count[0][0])
        
        for i in range(1, len(sorted_sum_count)):
            if sorted_sum_count[i][1]==most_frq:
                result.append(sorted_sum_count[i][0])
            elif sorted_sum_count[i][1]<most_frq:
                break
        
        
        return result
        
            
        
        
        