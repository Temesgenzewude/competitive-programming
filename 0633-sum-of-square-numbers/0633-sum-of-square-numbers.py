class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left, right=0, int(math.sqrt(c))
        while left <= right:
            a2=left*left
            b2=right*right
            
            if a2 + b2==c:
                return True
            elif a2+b2 < c:
                left+=1
            elif a2+b2 > c:
                right-=1
        return False