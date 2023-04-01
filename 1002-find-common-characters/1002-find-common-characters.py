class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        total_counts=[1000000]*26
        
        for word in words:
            curr_count=[0]*26
            for c in word:
                curr_count[ord(c)-ord("a")]+=1
                
            for c in range(26):
                total_counts[c]=min(total_counts[c], curr_count[c])
        
        result=[]
                
        for c in range(26):
            for _ in range(total_counts[c]):
                result.append(chr(c+ord("a")))
        return result
                

        