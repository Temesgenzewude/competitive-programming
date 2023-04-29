"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def bfs(node):
            if not node:
                return 0
            depth=0
            que=deque()
            que.append(node)
            
            while que:
                level_len=len(que)
                
                for _ in range(level_len):
                    currNode=que.popleft()
                    for child in currNode.children:
                        que.append(child)
                depth+=1
            
            return depth
        
        
        return bfs(root)
        