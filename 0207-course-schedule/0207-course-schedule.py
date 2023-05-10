class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        
        
        def topSort(graph, indgrees,n):
            que=deque()
            
            for i in range(len(indgrees)):
                if indgrees[i]==0:
                    que.append(i)
                    
            
            
            courses=[]
            
            while que:
                course=que.popleft()
                if indgrees[course]==0:
                    courses.append(course)
                
                for neighbor in graph[course]:
                    indgrees[neighbor]-=1
                    if indgrees[neighbor]==0:
                        que.append(neighbor)
            
            return len(courses)==n
        
        
        graph=defaultdict(list)
        
        indgrees=[0 for _ in range(numCourses)]
        
        
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            
            indgrees[course]+=1
            
        return topSort(graph, indgrees, numCourses)
        
        
        
       
        
        
            
            
            
        
         
        
    
        
        
    
        