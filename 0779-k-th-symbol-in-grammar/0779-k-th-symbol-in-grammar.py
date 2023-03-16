class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def helper(n,k):
            if n==1:
                return 0
            if k%2==0:
                return 1-helper(n-1, (k+1)//2)
            elif k%2!=0:
                return helper(n-1,(k+1)//2)
            
            
#         def replace(s):
#             newS=""
            
#             for let in s:
#                 if let=="0":
#                     newS+="01"
#                 elif let=="1":
#                     newS+="10"
#             return newS
#         result=helper(n)
#         return int(result[k-1])
        
        return helper(n,k)
            
            
        
            
        
        