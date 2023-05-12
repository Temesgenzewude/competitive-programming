class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph=defaultdict(list)
        
        for rich,poor in richer:
            graph[poor].append(rich)
        
        answer = []
        for i in range(len(quiet)):
            quietest = quiet[i]
            person = i
            
            queue = deque([i])
            visited = set([i])
            while queue:
                curr = queue.popleft()
                if quiet[curr] < quietest:
                    quietest = quiet[curr]
                    person = curr
                for n in graph[curr]:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
            
            answer.append(person)
        
        return answer