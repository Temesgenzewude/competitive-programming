class Solution:
    def totalFruit(self, s: List[int]) -> int:
        r=l=mx=0
        mp = {}
        while r < len(s):
            if s[r] not in mp:
                mp[s[r]] = 1
            else:
                mp[s[r]] +=1
            
            if len(mp) <= 2:
                mx= max(mx,r-l+1)
            else:
                mp[s[l]] -=1
                while mp[s[l]] != 0:
                    l+=1
                    mp[s[l]]-=1
                mp.pop(s[l])
                l+=1
            r +=1
        return mx