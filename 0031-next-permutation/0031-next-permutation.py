class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        
        n =len(nums)
        if n <=2:
            return nums.reverse()
        
        ptr=n-2
        while ptr >=0 and nums[ptr] >= nums[ptr+1]:
            ptr-=1
        if ptr ==-1:
            return nums.reverse()
        
        for j in range(n-1, ptr, -1):
            if nums[ptr]  < nums[j]:
                nums[ptr], nums[j]=nums[j], nums[ptr]
                break
        nums[ptr+1:]= reversed(nums[ptr+1:])
                
        
        