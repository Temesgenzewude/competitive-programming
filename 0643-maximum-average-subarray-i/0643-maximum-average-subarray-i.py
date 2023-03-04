class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum=0
        maxSum=0
        i, j=k, 0
        m=s=sum(nums[:k])
        n=len(nums)
        if n <=1:
            return nums[0]/k

    
        while i<n:
            s=s+nums[i]-nums[j]
            m=max(s, m)

            j+=1
            i+=1
        return m/k
#         max_avr=-float("inf")
#         sub_sum=0
#         n=len(nums)
        
#         for i in range(k):
#             sub_sum+=nums[i]
#             max_avr=max(max_avr, sub_sum/k)
            
            
            
            
            
            
        
#         for i in range(n-k):
#             sub_sum=sub_sum - nums[i] + nums[i+k]
#             max_avr=max(max_avr, sub_sum/k)
            
        
#         return max_avr
    
            
            
        