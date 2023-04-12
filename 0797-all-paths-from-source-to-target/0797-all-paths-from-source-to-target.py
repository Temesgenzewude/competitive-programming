class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        adj_lst={i:[] for i in range(n)}
        

        
        paths=[]
        
        for i in range(len(graph)):
            for ele in graph[i]:
                adj_lst[i].append(ele)
        print(adj_lst)
        
        def dfs(node, path):
            
            if node == n-1:
                paths.append(path[:])
               
            for neighbour in adj_lst[node]:
                path.append(neighbour)
                dfs(neighbour,path)
                path.pop()
        
      
        dfs(0, [0])
                
        return paths
        