class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo=0
        hi= len(nums)-1
        mid = (lo + hi)//2
        
        mid_val= nums[mid]
        
        if target > nums[hi]:
            return hi+1
        if target < nums[lo]:
            return lo
        
        while lo <= hi:
            
        
            
            if mid_val== target:
                return mid
            elif mid_val > target:
                hi= mid - 1
                if nums[hi] < target:
                    return hi+1
            elif mid_val < target:
                lo= mid +1
                if nums[lo] > target:
                    return lo
            mid = (lo + hi)//2
            mid_val= nums[mid]
            
        