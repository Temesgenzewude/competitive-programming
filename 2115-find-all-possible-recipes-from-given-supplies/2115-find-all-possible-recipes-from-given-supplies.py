class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        
        def topSort():
            graph=defaultdict(list)
            incoming=defaultdict(int)
            supply=set(supplies)

            
            for i in range(len(recipes)):
              
                for ing in ingredients[i]:
                    graph[ing].append(recipes[i])
                    incoming[recipes[i]]+=1
            
            que=deque(supplies)
            
            prepared=[]
            
    
            
            while que:
                rec=que.popleft()
                if rec not in supply and incoming[rec]==0:
                    prepared.append(rec)
                    
                for neighbour in graph[rec]:
                    incoming[neighbour]-=1
                    if incoming[neighbour]==0:
                        que.append(neighbour)
            
            return prepared
        
        
        return topSort()
        
                    
                    
                    
                
                
                
                
                
        
                    
                    
                
        
        
        

            
            
        
        
        