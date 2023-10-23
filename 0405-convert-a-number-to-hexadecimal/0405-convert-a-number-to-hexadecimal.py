class Solution:
    def toHex(self, num: int) -> str:
        if num<0: num+=2**32
        ans=("%x"% num)
        return ans