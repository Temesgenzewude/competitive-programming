
class TrieNode:
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.isEnd=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self, word):
        curr=self.root
        
        for char in word:
            idx=ord(char)-ord('a')
            
            if not curr.children[idx]:
                curr.children[idx]=TrieNode()
            curr=curr.children[idx]
            
        curr.isEnd=True
        
    def search(self, curr, word):
        
        for i, char in enumerate(word):
            if char == '.':
                for child in curr.children:
                    if child and self.search(child,  word[i+1:]):
                        return True
                return False
            idx=ord(char)-ord('a')

            if not curr.children[idx]:
                return False

            curr=curr.children[idx]
        return curr.isEnd
        

class WordDictionary:

    def __init__(self):
        self.trie=Trie()
        

    def addWord(self, word: str) -> None:
        
        self.trie.insert(word)
    
    def search(self, word: str) -> bool:
        
        return self.trie.search(self.trie.root, word)
    
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)