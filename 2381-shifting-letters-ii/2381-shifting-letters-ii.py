class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        #for forward shift 
        char=chr(((ord(letter)-97 +1)%26)+97)
        # for backward shift
        char=chr(((ord(letter)-97 - 1)%26)+97)
        """
        
        answer=[]
        currShift=0
        prefixSum=[0]*(len(s)+1)
        
        for start, end, direction in shifts:
            diff=1 if direction else -1
            
            prefixSum[start]+=diff
            prefixSum[end+1]-=diff
        for idx, char in enumerate(s):
            currShift=(currShift + prefixSum[idx])%26
            num=(ord(s[idx]) - ord("a")+ 26 +currShift)%26
            answer.append(chr(num + ord("a")))
        
        return "".join(answer)
        
        
        

        
        