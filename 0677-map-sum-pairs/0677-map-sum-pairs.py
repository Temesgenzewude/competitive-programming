class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dic = {}
        

    def insert(self, key: str, val: int) -> None:
        delta = val - self.dic.get(key, 0)
        self.dic[key] = val
        node = self.root
        node.freq += delta
        for symbol in key:
            node = node.children.setdefault(symbol, TrieNode())
            node.freq += delta
        

    def sum(self, prefix: str) -> int:
        node = self.root
        for symbol in prefix:
            if symbol not in node.children:
                return 0
            node = node.children[symbol]
        return node.freq
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)