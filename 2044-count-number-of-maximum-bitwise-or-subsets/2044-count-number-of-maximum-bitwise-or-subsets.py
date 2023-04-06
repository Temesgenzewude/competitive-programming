class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or=0
        count=0
        
        for i in range(len(nums)):
            max_or |= nums[i]
            
        total_subsets=2**len(nums)
        
        
        for i in range(total_subsets):
            subset_or=0
            
            for j in range(len(nums)):
                if (i & (1<<j)):
                    subset_or |= nums[j]
            if subset_or==max_or:
                count+=1
        return count
                
        