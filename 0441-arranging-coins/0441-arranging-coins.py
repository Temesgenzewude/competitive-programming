class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans= bisect_left(range(1,n),n,key=lambda x:x*(x+1)//2)+1
        if ans*(ans+1)//2==n:
            return ans
        return ans-1