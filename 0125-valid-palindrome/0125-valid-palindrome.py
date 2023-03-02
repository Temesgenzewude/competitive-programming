class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=[]
        
        for word in s:
            if word.isalnum():
                st.append(word)
        
        out= "".join(st)
        out=out.lower()
        
        
        left=0
        right=len(out)-1
        
        while right>=left:
            if out[right] !=out[left]:
                return False
            else:
                left+=1
                right-=1
        return True
        
        
        
        
                
        
      
                
        
        