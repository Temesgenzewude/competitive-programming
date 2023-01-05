class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # for i in range(k):
        #     last= nums.pop()
        #     nums.insert(0, last)
        
        
        # rotate the last k element
        
        k = k % len(nums)
            
        left= len(nums)-k
        right= len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right-=1
            
        # rotate the first n-k elements
        left= 0
        right= len(nums)-k-1
        while left < right:
            nums[left], nums[right]= nums[right], nums[left]
            left+=1
            right-=1
            
        # rotate the entire array
        left =0
        right= len(nums)-1
        while left < right:
            nums[left], nums[right]= nums[right], nums[left]
            left+=1
            right-=1
        
        
        