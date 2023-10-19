class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Step 1
        is_prime = [True] * n
        
        # Step 2
        is_prime[0] = is_prime[1] = False
        
        # Step 3
        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        # Step 4
        return sum(is_prime)
        
        