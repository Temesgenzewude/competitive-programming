class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lo = hi = 0
        ans = 1
        freq = {}
        while(hi < len(s)):
            while(lo < hi and s[hi] in freq):
                del freq[s[lo]]
                lo += 1
            ans = max(ans, hi - lo + 1)
            freq[s[hi]] = True
            hi += 1
        return ans