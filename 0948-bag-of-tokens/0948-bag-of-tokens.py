class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        que= deque(sorted(tokens))
        
        score=0
        max_score=0
        
        while que:
            if power >= que[0]:
                temp= que.popleft()
                power-=temp
                score+=1
                
                max_score=max(score, max_score)
            elif score > 0:
                temp= que.pop()
                power+=temp
                score-=1
            else: break
        
        return max_score
                
                
                
                
        