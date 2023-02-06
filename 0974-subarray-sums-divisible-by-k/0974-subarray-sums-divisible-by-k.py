class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sub_sum=0
        n=len(nums)
        result=0
        rem_map={0:1}
        
        for i in range(n):
            sub_sum+=nums[i]
            
            rem=sub_sum%k
            
            if rem <0:
                rem+=k
            
            if rem in rem_map:
                result+=rem_map.get(rem)
            rem_map[rem]= 1+ rem_map.get(rem, 0)
        
        
        return result
                
        