class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        res=""
        flg=0
        if num<0:
            flg=1
        num=abs(num)
        while(num>0):
            res+=str(num%7)
            num//=7
        if flg==1:
            res+="-"
        return res[::-1]