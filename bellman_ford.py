
def bellmanFord():
    n,m= list(map(int, input().split()))

    distances=[float('inf') for _ in range(n+1)]

    distances[1]=0


    graph=[]

    for _ in range(m):
        graph.append(list(map(int, input().split())))

    for _ in range(n-1):
        for edge in graph:
            src, dst, length= edge

            if distances[src]+ length < distances[dst]:
                distances[dst]= distances[src]+ length

    for dist in distances[1:]:
        print(dist if dist != float('inf') else 30000, end=" ")

bellmanFord()



    