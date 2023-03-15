class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s):
            newS=list(s)
            for i in range(len(newS)):
                if newS[i]=="0":
                    newS[i]="1"
                elif newS[i]=="1":
                    newS[i]="0"
            return "".join(newS)
        
        def helper(n):
            if n==1:
                return "0"
            si=helper(n-1)
            
            return si + "1" + (invert(si)[::-1])
        
        
        result= helper(n)
        
        return result[k-1]
        