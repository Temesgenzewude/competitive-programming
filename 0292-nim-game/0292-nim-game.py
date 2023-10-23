def can_win(n: int, cache: dict[int, bool]) -> bool:
    if n in cache:
        return cache[n]
    cache[n - 1] = can_win(n - 1, cache)
    cache[n - 2] = can_win(n - 2, cache)
    cache[n - 3] = can_win(n - 3, cache)
    return not (cache[n - 1] and cache[n - 2] and cache[n - 3])

class Solution:
   
    def canWinNim(self, n: int) -> bool:
        
        if n >= 134882061:
            
            return n % 4 != 0
        cache = {1: True, 2: True, 3: True, 4: False}
        return can_win(n, cache)
        