
def negativeCycle():
    n,m = list(map(int,input().split()))

    graph=[]

    for _ in range(m):
        graph.append(list(map(int,input().split())))
    
   

    distance = [float('inf') for _ in range(n+1)]
    distance[1] = 0

    if n == 1:
        print("YES")
        print(*graph[0][:2])
        return
    

    parent = [-1 for _ in range(n+1)]

    for _ in range(n-1):
        for edge in graph:
            src,dst,length = edge
            parent[dst] = src
            if  distance[src] + length < distance[dst]:
                distance[dst] = distance[src] + length
                
    
    
    print('graph',graph) 
    print('distance',distance)
    print('parent',parent)   
    
    for edge in graph:
        src,dst,length = edge
        if  distance[src] + length < distance[dst]:
            print("YES")
            cycle = [src]
            print('cycle start', src)
            node = parent[src]
            while node!=-1 and node not in cycle:
                print('cycle node', node)

                cycle.append(node)
                node = parent[node]
            cycle.append(node)

            print('cycle end', node)
            print(*cycle[::-1])
            # cycle = cycle[cycle.index(node):]
            
            # print(" ".join(str(node) for node in cycle[::-1]))
            return
    
    print("NO")
    
negativeCycle()






    


    



