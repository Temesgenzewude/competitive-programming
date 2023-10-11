

class TrieNode:
    def __init__(self):
        self.children=[None]*2
        self.isEnd=False

class Trie:
    
    def __init__(self):
        self.root= TrieNode()
    def insert(self,num):
        curr= self.root
        for i in range(31, -1, -1):
            bit = (num>>i) & 1
            
            if curr.children[bit]==None:
                curr.children[bit]=TrieNode()
            curr= curr.children[bit]
        curr.isEnd=True
    def search(self, num):
        curr= self.root
        ans=0
        for i in range(31, -1,-1):
            bit= (num>>i) & 1
            if curr.children[1-bit]:
                ans+=(1<<i)
                curr= curr.children[1-bit]
            else:
                curr=curr.children[bit]
        
        return ans
    

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        # quickly determine the leftmost 1
        leftmost_one, max_num = 0, max(nums)
        while max_num:
            leftmost_one += 1
            max_num >>= 1
                    
        mask, max_xor = 0, 0
        for i in reversed(range(leftmost_one)): # use the leftmost 1 to skip the leading 0s
            mask |= 1 << i
            next_max_xor = max_xor | 1 << i
            prefixes = {num & mask for num in nums}
            candidates = [num for num in nums if (num & mask) ^ next_max_xor in prefixes]
            
            if candidates:
                nums = candidates # discard all numbers that are no longer relevant
                max_xor = next_max_xor
            
        return max_xor
        
#         maxXor=0
#         trie= Trie()
        
        
#         for num in nums:
#             trie.insert(num)
#             maxXor= max(maxXor,trie.search(num))
        
#         return maxXor
    
