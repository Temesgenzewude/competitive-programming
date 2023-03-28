class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        answer=[0]*len(nums)
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if nums[j]< nums[i]:
#                     result[i]+=1
        
#         return result
    
        def mergeSort(left,right,arr):
            if left==right:
                return [(arr[left],left)]
            mid=left + (right-left)//2
            
            left_half=mergeSort(left,mid, arr)
            right_half=mergeSort(mid+1, right,arr)
            
            return merge(left_half, right_half)
        
        def merge(left_half, right_half):
            right=0
            
            smallers=0
            
            for i in range(len(left_half)):
                while right < len(right_half) and left_half[i][0] > right_half[right][0]:
                    smallers+=1
                    right+=1
                answer[left_half[i][1]]+=smallers
                
            
            
            result=[]
            left_ptr=right_ptr=0
            
            while left_ptr < len(left_half) and right_ptr < len(right_half):
                if left_half[left_ptr][0] <=right_half[right_ptr][0]:
                    result.append((left_half[left_ptr][0], left_half[left_ptr][1]))
                    left_ptr+=1
                else:
                    result.append((right_half[right_ptr][0], right_half[right_ptr][1]))
                    right_ptr+=1
                    
            
            result.extend(left_half[left_ptr:])
            result.extend(right_half[right_ptr:])
            
            return result
        
        
        mergeSort(0, len(nums)-1, nums)
        
        
        return answer
    
                    
        