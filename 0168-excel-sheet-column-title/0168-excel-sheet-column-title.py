class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c=columnNumber
        m=''
        while c:
            c-=1
            r=c%26
            c//=26
            m=chr(65+r)+m
        return m
        