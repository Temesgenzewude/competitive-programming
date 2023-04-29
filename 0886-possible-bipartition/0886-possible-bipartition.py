class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        dic={}
        
        for pairs in dislikes:
            if pairs[0] in dic:
                dic[pairs[0]].add(pairs[1])
            else:
                dic[pairs[0]]=set([pairs[1]])
            
            if pairs[1] in dic:
                dic[pairs[1]].add(pairs[0])
            else:
                dic[pairs[1]]=set([pairs[0]])
                
        
        visited={}
        
        for i in range(1, n+1):
            if i not in visited:
                visited[i]=0
                stack=[i]
                
                while stack:
                    a=stack.pop()
                    if a in dic:
                        for b in dic[a]:
                            if b in visited :
                                if visited[a]==visited[b]:
                                    return False
                            else:
                                
                                visited[b]=(visited[a]+1)%2
                                stack.append(b)
        
        return True
    
        