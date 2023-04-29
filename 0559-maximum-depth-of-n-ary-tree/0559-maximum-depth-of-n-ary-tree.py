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
        self.max_depth=0
        
        def dfs(node, depth):
            if not node:
                return
            
            self.max_depth=max(self.max_depth, depth)
            
            for child in node.children:
                dfs(child, depth+1)
        
        dfs(root, 1)
        return self.max_depth
            
        
        
       
        