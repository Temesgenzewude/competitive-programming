class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixSum=[0]*(len(arr)+1)
        result=[]
        
        for i in range(len(arr)):
            
            prefixSum[i+1]= prefixSum[i] ^ arr[i]
            
        
        for i in range(len(queries)):
            query= queries[i]
            right, left=query[1], query[0]
            result.append((prefixSum[right+1] ^ prefixSum[left]))
        
    
        return result
           
                          
            
            
        
        