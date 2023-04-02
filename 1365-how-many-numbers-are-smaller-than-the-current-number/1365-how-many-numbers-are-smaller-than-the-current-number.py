class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        
        
        for i in range(len(nums)):
            curr_num=nums[i]
            
            for j in range(len(nums)):
                if  j !=i and curr_num > nums[j]:
                    ans[i]+=1
        return ans
        
#         def mergeSort(left, right,arr):
#             if left==right:
#                 return [(arr[left], left)]
#             mid=left+ (right-left)//2
            
#             left_half=mergeSort(mid, left, arr)
#             right_half=mergeSort(mid+1, right,arr)
            
#             return merge(left_half, right_half)
        
#         def merge(left_half, right_half):
            
            
#             right=0
            
#             for left in range(len(left_half)):
#                 while 
            
            
            
            
#             left_ptr=right_ptr=0
            
            
#             result=[]
#             while left_ptr < len(left_half) and right_ptr < len(right_half):
#                 if left_half[left_ptr] <= right_half[right_ptr]:
#                     result.append(left_half[left_ptr])
#                     left_ptr+=1
#                 else:
#                     result.append(right_half[right_ptr])
#                     right_ptr+=1
            
#             result.extend(left_half[left_ptr:])
#             result.extend(right_half[right_ptr:])
            
            
#             return result
                    
        