class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
       
        graph=defaultdict(list)
        answer=[False for _ in range(len(queries))]
        
        

        for pre, course in prerequisites:
            graph[course].append(pre)
            
        pres={}
        
            
        
        def dfs(course):
            
            if course not in pres:
                pres[course]=set()
                for nei in graph[course]:
                    pres[course] |= dfs(nei)
                pres[course].add(course)
            return pres[course]
        
        for course in range(numCourses):
            dfs(course)
  
         
        for i in range(len(queries)):
            if queries[i][1] in pres and queries[i][0] in pres[queries[i][1]]:
                answer[i]=True  
        return answer
            
            
            
            
      