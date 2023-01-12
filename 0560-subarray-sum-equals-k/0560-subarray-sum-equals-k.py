class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        slow=fast=0
        prefixSum={0:1}
    
        
        count=0
        curr_sum=0
        
                
        for num in nums:
            
            curr_sum+=num
            diff=curr_sum -k
            count+=prefixSum.get(diff, 0)
            prefixSum[curr_sum]=1+prefixSum.get(curr_sum, 0)
          
        return count
       
        
#         for num in nums:
#             curr_sum+=num
#             if curr_sum==k:
#                 count+=1
#             if curr_sum -k in dic:
#                 dic[curr_sum - k]+=1
#                 count+=1
            
#             dic[curr_sum]=1
#         return count
            
            
      
            
        
#         while slow <=fast and fast < n:
#             if sub_sum==k:
#                 count+=1
#                 fast+=1
#                 sub_sum=sub_sum - nums[slow] + nums[fast]
#                 slow+=1
#             elif sub_sum < k:
#                 fast+=1
#                 sub_sum+=nums[fast]
#             else:
#                 slow+=1
#                 sub_sum-=nums[slow]
                
#         return count
            
            
        
        