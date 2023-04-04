def cirno():
    tests=int(input())
    
    
    for _ in range(tests):
        x=int(input())
        y=0
        
        # for i in range(1, (2**30)+1):
        #     if x & i >0 and x ^ i >0:
        #         print(i)
        #         break
        
        for i in range(31):
            if ((x >> i) & 1) ==1:
                y |= (1 <<i)
                break
        
        if x & y > 0 and x ^ y > 0:
            print(y)
        else:
            for i in range(31):
                if ((x >> i) & 1)==0:
                    y |= (1 <<i)
                    break
            print(y)
        
        
        
cirno()
