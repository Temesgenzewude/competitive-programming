class Solution:
    def reverseWords(self, s: str) -> str:

        s=s.strip().split()
        left=0
        right=len(s)-1
        
        while left<= right:
            s[left], s[right]=s[right],s[left]
            left+=1
            right-=1
        
        s= " ".join(s)
        
        return s
        
       
        