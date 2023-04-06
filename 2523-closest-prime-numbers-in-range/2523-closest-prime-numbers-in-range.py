class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime=[True for _ in range(right+1)]
        isPrime[0], isPrime[1]=False, False
        
        for i in range(right+1):
            if isPrime[i]:
                for j in range(i*i, right+1, i):
                    isPrime[j]=False
        primes=[]
        for k in range(left, right+1):
            if isPrime[k]:
                primes.append(k)
        result=[-1,-1]
        
        min_diff=math.inf
        
        for i in range(len(primes)-1):
            diff=primes[i+1]-primes[i]
            pair=[primes[i], primes[i+1]]
            
            if min_diff > diff:
                min_diff=diff
                result=pair
            elif min_diff==diff and result[0] > pair[0]:
                result=pair
        return result
#         secondPrime=-1
#         firstPrime=-1
        
#         result=[firstPrime, secondPrime]
        
        
#         def isPrime(n):
#             d=2
#             while d*d <=n:
#                 if n %d==0:
#                     return False
#                 d+=1
#             return True

        
#         for i in range(left, right+1):
#             if isPrime(i):
#                 firsPrime=i
#                 break
#         if firstPrime !=-1:
#             for j in range(firstPrime+1, right+1):
#                 if isPrime(j):
#                     secondPrime=j
#         else:
#             return [-1,-1]
        
#         return result
        
                
        
        
        