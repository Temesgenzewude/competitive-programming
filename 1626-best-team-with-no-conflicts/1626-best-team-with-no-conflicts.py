class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        pairs= [[scores[i], ages[i]] for i in range(len(scores))]
        
        pairs.sort()
        
        dp=[pairs[i][0] for i in range(len(pairs))]
        
        for i in range(len(pairs)):
            maxScore, maxAge= pairs[i]
            for j in range(i):
                score, age= pairs[j]
                
                if maxAge>= age:
                    dp[i]=max(dp[i], maxScore+ dp[j])
                    
        
        
        return max(dp)
                
        