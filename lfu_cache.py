
import collections


class Node:
    def __init__(self,key, val):
        self.key=key
        self.val=val
        self.freq=1
        self.next=self.prev=None
class DLinkedList:
    def __init__(self):
        self.dummyHead=Node(None, None)
        self.dummyTail=Node(None, None)
        self.dummyHead.next=self.dummyTail
        self.dummyTail.prev=self.dummyHead
        self._size=0
        
        
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next=self.dummyHead.next
        node.prev=self.dummyHead
        self.dummyHead.next.prev=node
        self.dummyHead.next=node
        self._size+=1
        
    def popLRU(self):
        if self._size == 0: return None
        else:
            LRUNode=self.dummyTail.prev
            self.dummyTail.prev=LRUNode.prev
            LRUNode.prev.next=self.dummyTail
            self._size -=1
            return LRUNode
    def pop(self,givenNode):
        if self._size== 0: return None
        else:
            givenNode.prev.next=givenNode.next
            givenNode.next.prev=givenNode.prev
            self._size -=1
        return givenNode
        
            
        
            
            
        
        
    


class LFUCache:

    def __init__(self, capacity: int):
        self._cap=capacity
        self._node={}
        self._freq=collections.defaultdict(DLinkedList)
        self.min_freq=0
        self._size=0
    def update(self, key):
        aNode=self._node[key]
        aFreq=aNode.freq
        oldDLinkedList=self._freq[aFreq]
        oldDLinkedList.pop(aNode)
        
        if self.min_freq == aFreq and not self._freq[aFreq]:
            self.min_freq+=1
        aNode.freq+=1
        newDLinkedList=self._freq[aNode.freq]
        newDLinkedList.pop(aNode)
        
            
        
        

    def get(self, key: int) -> int:
        if self._node.get(key) != None:
            self.update(key)
            return self._node[key].val
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if self._cap == 0: return
        if self._node.get(key) != None:
            self._node[key].val= value
            self.update(key)
        else:
            if self._size == self._cap:
                LRU=self._freq[self.min_freq].popLRU()
                self._size -=1
                self._node.pop(LRU.key)
        newNode= Node(key, value)
        self._node[key]=newNode
        self._freq[1].append(newNode)
        self.min_freq=1
        self._size+=1
        
        
        
                
                
            
            
        
        
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)