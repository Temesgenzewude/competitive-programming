class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        graph=defaultdict(list)
        
        for room in range(len(rooms)):
            for key in rooms[room]:
                graph[room].append(key)
        
        print(graph)
                
        
        def bfs(graph, node):
            visited=set([node])
            que=deque([node])
            
            
            while que:
                node=que.popleft()
                
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        que.append(neighbour)
            
            return len(visited)==len(rooms)
            
                        
        return bfs(graph, 0)
        
        
                        
        
       
            
                        
        