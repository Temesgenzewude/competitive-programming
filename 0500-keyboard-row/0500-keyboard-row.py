class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = 'qwertyuiop'
        r2 = 'asdfghjkl'
        r3 = 'zxcvbnm'
        l1=[]
        c1, c2, c3 = 0, 0, 0
        for i in words:

            for j in i.lower():
                if j in r1:
                    c1 += 1
                elif j in r2:
                    c2 += 1
                elif j in r3:
                    c3 += 1

            if c1 == len(i) or c2 == len(i) or c3 == len(i):
                l1.append(i)

            c1, c2, c3 = 0, 0, 0
        return l1