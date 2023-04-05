class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
 
        n = len(words)
        nums = [0] * n
        for i in range(n):
            for c in words[i]:
                nums[i] |= 1 << (ord(c) - ord('a'))
        
        max_product = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] & nums[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product
#         words_set=[set(word) for word in words]
        
#         max_pro=0
        
        
#         for idx1 in range(len(words_set)):
            
#             for idx2 in range(len(words_set)):
#                 valid=True
                
#                 for let in words_set[idx2]:
#                     if let in words_set[idx1]:
#                         valid=False
#                         break
#                 if valid:
#                     max_pro=max(max_pro, len(words[idx1]* len(words[idx2])))
                    
            
        
#         return max_pro
    
        