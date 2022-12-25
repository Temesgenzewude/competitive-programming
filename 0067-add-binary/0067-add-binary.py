class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_i, b_i= 0,0
        
        for i in range(len(a)):
            a_i+= (int(a[i]) * (2 ** (len(a) -1-i )))
        for i in range(len(b)):
            b_i += (int(b[i]) * (2**(len(b)-1-i )))
        
        print(a_i, b_i)
        print(bin(a_i + b_i))
        return '{0:b}'.format((a_i + b_i))
        