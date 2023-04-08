class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        winningPost=0
        for i in range(2, n+1):
            winningPost=((winningPost+k)% i)
        
        return winningPost + 1
        