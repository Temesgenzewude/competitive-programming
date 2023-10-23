class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        st=""
        s=s.replace("-","").upper()
        s=s[::-1]
    
        for i in range(0,len(s),k):
            st+=s[i:i+k]
            st+="-"
        sts=st[::-1]
       
        sts=sts.replace("-","",1)
        return sts