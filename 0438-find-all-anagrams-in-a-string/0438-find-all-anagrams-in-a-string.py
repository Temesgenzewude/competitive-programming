class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s): return []
        pCount, sCount={},{}
        
        for i in range(len(p)):
            pCount[p[i]]=1+pCount.get(p[i], 0)
            sCount[s[i]]=1+sCount.get(s[i], 0)
        
        result=[0] if sCount==pCount else []
        
        left=0
        for right in range(len(p), len(s)):
            sCount[s[right]]=1+sCount.get(s[right],0)
            sCount[s[left]]-=1
            
            if sCount[s[left]]==0:
                sCount.pop(s[left])
            left+=1
            if sCount==pCount:
                result.append(left)
        return result
        
#         def isAnagram(subString):
#             p_count=dict()
#             for letter in p:
#                 p_count[letter]=1+p_count.get(letter,0)
                
#             if len(subString)==len(p):
#                 sub_count=dict()
                
                
#                 for let in subString:
#                     sub_count[let]=1+sub_count.get(let, 0)
#                 for key in p_count:
#                     if key not in sub_count or p_count[key] != sub_count[key]:
#                         return False
                
#             else:
#                 return False
            
#             return True
        
        
#         k=len(p)
#         result=[]
#         n=len(s)
    
        
#         for i in range(n-k+1):
#             sub_string=s[i: i+k]
#             if isAnagram(sub_string):
#                 result.append(i)
#         return result
            
            
            
            
            
        
                
                    
                    
                    
                
                
        
        