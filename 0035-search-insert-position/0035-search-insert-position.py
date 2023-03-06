class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        
        def isGreaterOrEqual(mid_num):
            if mid_num >=target:
                return True
            else:
                return False
        low=-1
        high=len(nums)
        
        while high > low+1:
            mid= low + (high-low)//2
            
            mid_num=nums[mid]
            
            if isGreaterOrEqual(mid_num):
                high=mid
            else:
                low=mid
        
        return high
        
        
#         lo=0
#         hi= len(nums)-1
#         mid = (lo + hi)//2
        
#         mid_val= nums[mid]
        
#         if target > nums[hi]:
#             return hi+1
#         if target < nums[lo]:
#             return lo
        
#         while lo <= hi:
            
        
            
#             if mid_val== target:
#                 return mid
#             elif mid_val > target:
#                 hi= mid - 1
#                 if nums[hi] < target:
#                     return hi+1
#             elif mid_val < target:
#                 lo= mid +1
#                 if nums[lo] > target:
#                     return lo
#             mid = (lo + hi)//2
#             mid_val= nums[mid]
      
                
                
                
                
                
                
        
            
            
        