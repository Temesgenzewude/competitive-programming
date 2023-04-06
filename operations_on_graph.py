from collections import defaultdict
def operationsOnGraph():
    n=int(input())
    graph=defaultdict(list)
    
    opes=int(input())
    
    for _ in range(opes):
        opes=list(map(int, input().split()))
        
        if len(opes)==3:
            graph[opes[1]].append(opes[2])
            graph[opes[2]].append(opes[1])
        else:
            adj=graph[opes[1]]
            for a in adj:
                print(a, end=" ")
            print()

operationsOnGraph()
