class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        
        result=""
        
        while word1 and word2:
            if word1 > word2:
                result+=word1[0]
                word1=word1[1:]
            else:
                result+=word2[0]
                word2=word2[1:]
        result+=word1
        result+=word2
                
        return result
        