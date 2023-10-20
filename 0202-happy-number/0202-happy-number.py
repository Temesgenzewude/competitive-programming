
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visitedNumbers = set()
        while n not in visitedNumbers:
            visitedNumbers.add(n)
            n = self.squaring(n)
            if n == 1:
                return True
            
        return False
    
    def squaring(self,n):
        squareCount = 0
        while n > 0:
            numberMod = n % 10
            numberMod = numberMod * numberMod
            squareCount += numberMod
            n = n // 10
        return squareCount 