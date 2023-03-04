class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast=0,0
        
        uniq_chars=set()
        max_len=0
        
        while fast < len(s) and slow <=fast:
            if s[fast] not in uniq_chars:
                uniq_chars.add(s[fast])
                max_len=max(max_len, len(uniq_chars))
                fast+=1
            else:
                uniq_chars.remove(s[slow])
                max_len=max(max_len, len(uniq_chars))
                slow+=1
            
    
        return max_len
                
                
            
            
            
            
            
            
        