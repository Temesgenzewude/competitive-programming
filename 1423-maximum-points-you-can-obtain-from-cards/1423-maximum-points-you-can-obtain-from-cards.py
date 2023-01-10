class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        current=0
        result=0
        
        for i in range(-k, k):
            current+=cardPoints[i]
            
            if i >=0:
                current -= cardPoints[i -k]
            result=max(result, current)
        
        return result
        