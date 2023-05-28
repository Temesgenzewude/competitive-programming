def insertionSort1(n, arr):
    # Write your code here
    key = arr[-1]
    
    i=n-1
    while i>0 and arr[i-1]>key:
        arr[i]=arr[i-1]
        for ele in arr:
            print(ele, end=" ")
        print()
        i-=1
    arr[i]=key
    for ele in arr:
        print(ele, end=" ")
    print()
