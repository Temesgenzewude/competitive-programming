class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        cookies=sorted(cookies, reverse=True)
        
        
        def backtrack(i, kids):
            if i >=len(cookies):
                return max(kids)
            
        
        
            unfair=float("inf")
            for idx, kid in enumerate(kids):
                kids[idx]+=cookies[i]
                if kids[idx]<unfair:
                    unfair=min(unfair, backtrack(i+1, kids))
                    

                kids[idx]-=cookies[i]
            return unfair
        
        return backtrack(0, [0 for _ in range(k)])
    
    
    
    
            
        
            