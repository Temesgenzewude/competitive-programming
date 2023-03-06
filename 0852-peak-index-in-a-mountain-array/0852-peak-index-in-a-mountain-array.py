class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low=0
        high=len(arr)-1
        
        def isGreaterOrEqual(mid):
                              
            if arr[mid] >=arr [mid-1]:
                return True
            else:
                return False
        while high > low+1:
            mid = low+(high-low)//2
            if isGreaterOrEqual(mid):
                low=mid
            else:
                high=mid
        
        return low
                
                              
                              
                              
                              
                              
                
                              
        