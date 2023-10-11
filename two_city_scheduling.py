class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        diff=[]
        
        for costA, costB in costs:
            diff.append((costA, costB, costA-costB))
            
        diff.sort(key=lambda x:x[-1])
        
        mini_cost=0
        
        for i in range(len(costs)):
            if i < len(costs)//2:
                mini_cost+=diff[i][0]
            else:
                mini_cost+=diff[i][1]
        return mini_cost
