class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1
        
        def children(lock):
            result=[]
            
            for i in range(4):
                dig=str((int(lock[i])+1)%10)
                result.append(lock[:i]+dig + lock[i+1:])
                
                dig=str((int(lock[i])-1+10)%10)
                result.append(lock[:i]+dig + lock[i+1:])
                
            return result
        
        
        
        que=deque()
        visited=set(deadends)
        que.append(["0000",0])
        while que:
            lock, turns=que.popleft()
            if lock==target:
                return turns
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    que.append([child, turns+1])
        return -1
    

                
        
        
        