class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count={}
        s2Count={}
        
        for i in range(len(s1)):
            s1Count[s1[i]]=1+s1Count.get(s1[i], 0)
            s2Count[s2[i]]=1+s2Count.get(s2[i], 0)
        
        if s1Count==s2Count: return True
        
        left=0
        for right in range(len(s1), len(s2)):
            s2Count[s2[right]]=1+s2Count.get(s2[right],0)
            s2Count[s2[left]]-=1
            
            if s2Count[s2[left]]==0:
                s2Count.pop(s2[left])
            left+=1
            
            
            if s2Count==s1Count:
                return True
        
        return False
            
            
        
        
    
        
        
        