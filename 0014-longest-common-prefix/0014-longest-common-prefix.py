class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp=""
        if strs is None or len(strs)==0:
            return lcp
        
        minLeng= len(strs[0])
        
        
        for i in range(1, len(strs)):
            minLeng= min(minLeng, len(strs[i]))
        
        
        for k in range(minLeng):
            letter= strs[0][k]
            
            for j in range(1, len(strs)):
                if strs[j][k] != letter:
                    return lcp
            lcp+=letter
        
        return lcp

            
            
        