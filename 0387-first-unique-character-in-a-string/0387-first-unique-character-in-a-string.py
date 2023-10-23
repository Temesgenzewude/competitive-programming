class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        seen=set()
        for ind,let in enumerate(s):
            if let not in seen:
                dic[let]=ind
                seen.add(let)
            elif let in dic:
                del dic[let]
        return min(dic.values()) if dic else -1