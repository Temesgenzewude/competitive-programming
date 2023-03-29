class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        answer=[0]*(n+1)
        
        for i in range(0, n+1):
            
            curr=i
            
            while curr !=0:
                if curr %2==1:
                    answer[i]+=1
                curr=curr//2
        return answer
            
                
            
            
            
            
        
        