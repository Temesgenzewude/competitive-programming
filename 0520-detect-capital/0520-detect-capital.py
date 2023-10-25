class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.islower():
            return True
        elif word.isupper():
            return True
        else:
            if word[0].isupper():
                
                for i in range(1, len(word)):
                    if word[i].isupper():
                        return False
            else:
                return False
        
        return True
        
        