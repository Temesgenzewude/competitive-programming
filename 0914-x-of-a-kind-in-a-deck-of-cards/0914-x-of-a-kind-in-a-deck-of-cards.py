class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def gcd(a, b):
            if b==0:
                return a
            return gcd(b, a%b)
        
        
        counter=collections.Counter(deck)
        
        curr_gcd=0
        
        for count in counter.values():
            curr_gcd=gcd(curr_gcd, count)
            
        
        return curr_gcd >1
        