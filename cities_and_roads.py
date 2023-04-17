def citiesAndRoads():
    n=int(input())
    
    paths=0
    
    
    for i in range(n):
        row=list(map(int, input().split()))
        
        for j in range(len(row)):
            if row[j]==1:
                paths+=1
    print(paths//2)
citiesAndRoads()
