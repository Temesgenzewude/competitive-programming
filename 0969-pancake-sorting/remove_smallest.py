def removeSmallest():
    tests=int(input())

    for _ in range(tests):
        n=int(input())

        elements=list(map(int,input().split()))

        if n<=1:
            print("YES")
        else:
            elements.sort()

            left=0
            right=1
            moves=0

            while right <n:
                if elements[right] - elements[left] <= 1:
                    moves+=1
                left+=1
                right+=1
            if moves==n-1:
                print("YES")
            else:
                print("NO")
removeSmallest()
