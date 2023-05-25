class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        exchanges={5:0,10:0}
        
        
        for bill in bills:
            if bill==5:
                exchanges[bill]+=1
            elif bill==10:
                if exchanges[5] ==0:
                    return False
                else:
                    exchanges[5]-=1
                    exchanges[10]+=1
            else:
                if exchanges[5]==0:
                    return False
                elif exchanges[10] > 0:
                    exchanges[10]-=1
                    exchanges[5]-=1
                elif exchanges[5] >=3:
                    exchanges[5]-=3
                else:
                    return False
        return True
    
                        
                        
        