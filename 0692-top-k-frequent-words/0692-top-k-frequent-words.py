class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        dic={}
        
        for word in words:
            dic[word]=1+dic.get(word,0)
            
        
        return (sorted(dic.keys(), key=lambda word: (-dic[word], word)))[:k]
        
        
#         sorted_result=sorted(dic.items(), key=lambda kv: kv[1])
#         print(sorted_result)
        
#         n=len(sorted_result)
        
    
        
#         result=[]
#         for i in range(n-1, n-k-1, -1):
#             result.append(sorted_result[i][0])
            
        
#         for i in range(len(result)):
#             for j in range(i,len(result)):
#                 if dic[result[i]]== dic[result[j]] and result[i] > result[j]:
#                     result[i],result[j]=result[j], result[i]
                    
            
    
#         return result
            
        
            
            
        
        
        
        