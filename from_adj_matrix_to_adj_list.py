from collections import defaultdict
def fromAdjMatrixToAdjList():
    n=int(input())
    
    graph=defaultdict(list)
    
    for i in range(n):
        row= list(map(int, input().split()))
        
        for j in range(len(row)):
            
            if row[j]==1:
                graph[i+1].append(j+1)
    
    for i in range(n):
        print(len(graph[i+1]), end=" ")
        for j in range(len(graph[i+1])):
            print(graph[i+1][j], end=" ")
        print()
fromAdjMatrixToAdjList()
