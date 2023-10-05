class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) <=2:
            return len(nums)
        
        
        currIndex=2
        
        for i in range(2, len(nums)):
            if nums[i] != nums[currIndex-2]:
                nums[currIndex]=nums[i]
                currIndex+=1
        
        return currIndex
                
        