class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        def revers(i):
            num=nums[i]
            num=list(str(num))
            num=num[::-1]
            return int("".join(num))
        
        n=len(nums)
        
        for i in range(n):
            rev=revers(i)
            nums.append(rev)
        
      
        
        
        return len(set(nums))
    
    
        
        
        