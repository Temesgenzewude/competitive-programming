class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        n=len(skill)
        
        groups=n//2
        
        group_sum=sum(skill)//groups
        
        que=deque(skill)
        
        chemistry=0
        
        
        while que:
            first=que.popleft()
            second=que.pop()
            
            if first+second !=group_sum:
                return -1
            chemistry+=first*second
            
        return chemistry
            
        