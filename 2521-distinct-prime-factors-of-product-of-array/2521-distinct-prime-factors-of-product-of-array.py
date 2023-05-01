class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        is_prime=[True for _ in range(1001)]
        
        is_prime[0],is_prime[1]=False, False
        
        
        for x in range(2, 1001):
            if is_prime[x]:
                for i in range(x*x, 1001,x):
                    is_prime[i]=False
                    
        primes=[]
        
        for x in range(1001):
            if is_prime[x]:
                primes.append(x)
                
        
        factors=set()
        
        for x in nums:
            for p in primes:
                if x%p==0:
                    factors.add(p)
                
                if p > x:
                    break
        
        return len(factors)
                    
            
        