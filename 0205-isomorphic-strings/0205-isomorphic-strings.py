class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        
        seen = set()
        for i, j in zip(s, t):
            if i in d:
                if d[i] != j:
                    return False

            
            else:
                if j in seen:
                    return False

                seen.add(j)
                d[i] = j
                



        return True
        