from collections import defaultdict
def sourcesAndSinks():
    n=int(input())
    graph=[[0 for _ in range(n)] for _ in range(n)]
    
    
    
    for i in range(n):
        row=list(map(int, input().split()))
        
        for j in range(len(row)):
            graph[i][j]=row[j]
    sinks=[]
    sources=[]
    
    for  rw in range(n):
        isSink=True
        for cl in range(n):
            if graph[rw][cl]==1:
                isSink=False
                break
        if isSink:
            sinks.append(rw+1)
    for cl in range(n):
        isSource=True
        for rw in range(n):
            if graph[rw][cl]==1:
                isSource=False
                break
        if isSource:
            sources.append(cl+1)
     
    print(len(sources), end=" ")
    for source in sources:
        print(source, end=" ")
    print()
    
    print(len(sinks), end=" ")
    for sink in sinks:
        print(sink, end=" ")
    print()
    
       

sourcesAndSinks()
