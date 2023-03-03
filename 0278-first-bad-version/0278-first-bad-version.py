# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=0
        right=n
        while right >=left:
            mid=left + (right-left)//2
            
            if isBadVersion(mid):
                right=mid-1
            else:
                left=mid+1
        
        return left
                
        