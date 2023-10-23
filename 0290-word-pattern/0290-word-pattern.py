class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d, s2 = dict(), s.split()
        if len(pattern)!=len(s2): return False
        for (letter,word) in zip(pattern, s2):
            if letter in d:
                if d[letter]!=word:
                    return False
            elif word in d.values():
                return False
            else:
                d[letter] = word
        return True
        