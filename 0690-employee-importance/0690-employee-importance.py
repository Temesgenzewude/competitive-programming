"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        empMap={emp.id: emp for emp in employees}
        
        def dfs(emp):
            empImpo=empMap[emp].importance
            
            for sub in empMap[emp].subordinates:
                empImpo+=dfs(sub)
            return empImpo
        return dfs(id)
        