class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels="aeiou"
        max_vow= current_vow=0
        n=len(s)
        
    
        
        for i in range(k):
            if s[i] in vowels:
                current_vow+=1
                
        max_vow=max(max_vow, current_vow)
        
        
        for j in range(n-k):
            if s[j] in vowels and s[j+k] not in vowels:
                current_vow -=1
            elif s[j] not in vowels and s[j+k] in vowels:
                current_vow+=1
            else:
                current_vow=current_vow
            
            max_vow=max(max_vow, current_vow)
            
        return max_vow
            
                
        