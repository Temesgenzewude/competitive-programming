class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph=defaultdict(list)
        
        for u,v, w in times:
            
            graph[u].append((v, w))
           
        def dijkstra():
        
            times_to_receive=[float('inf')]*(n+1)
            visited=set()
            
            times_to_receive[k]=0
            
            queue= [(0, k)]
            
            while queue:
                currTime, currNode= heapq.heappop(queue)
                
                if currNode in visited or currTime > times_to_receive[currNode]:
                    continue
                
                visited.add(currNode)
                
                for dest, cost in graph[currNode]:
                    newTime= currTime+cost
                    
                    if newTime < times_to_receive[dest]:
                        times_to_receive[dest]=newTime
                        heapq.heappush(queue,(newTime, dest))
                        
            maxTime=float('-inf')
            for i in range(1,n+1):
                if times_to_receive[i] == float('inf'):
                    return -1
                maxTime=max(maxTime, times_to_receive[i])
            return maxTime
        
        return dijkstra()
                        
            
            
        
            
        