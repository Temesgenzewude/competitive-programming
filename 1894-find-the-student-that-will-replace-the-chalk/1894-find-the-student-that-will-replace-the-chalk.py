class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total=sum(chalk)
        mod=k % total
        current=chalk[0]
        n=len(chalk)
        
        i=0
        
        while i < n:
            if mod - chalk[i] >=0:
                mod-=chalk[i]
            else:
                return i
        
            i+=1
        return i
            
            
        
        