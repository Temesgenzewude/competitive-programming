class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_count={}
        result=0
        left=0
        for right in range(len(s)):
            char_count[s[right]]=1+char_count.get(s[right], 0)
            while (right-left +1)- max(char_count.values()) > k:
                char_count[s[left]]-=1
                left+=1
            result=max(result, right-left+1)
        
        
        return result
        