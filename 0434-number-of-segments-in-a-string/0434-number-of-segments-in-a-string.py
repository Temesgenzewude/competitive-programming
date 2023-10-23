class Solution:
    def countSegments(self, s: str) -> int:
        # Initialize the segment count to 0
        count = 0
        
        # Iterate over each character in the string
        for i in range(len(s)):
            # If the current character is not a space and the previous character is a space or it's the first character, increment the count
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                count += 1
        
        # Return the segment count
        return count