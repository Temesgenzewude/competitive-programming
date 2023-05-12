class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph=defaultdict(list)
        
        for rich,poor in richer:
            graph[poor].append(rich)
            
        def bfs(graph,node):
            quietest = quiet[node]
            person = node
            
            queue = deque([node])
            visited = set([node])
            while queue:
                curr = queue.popleft()
                if quiet[curr] < quietest:
                    quietest = quiet[curr]
                    person = curr
                for n in graph[curr]:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
            return person
        
        answer = []
        for node in range(len(quiet)):
            person=bfs(graph,node)
           
            answer.append(person)
        
        return answer