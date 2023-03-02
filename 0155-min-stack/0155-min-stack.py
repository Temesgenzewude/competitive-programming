class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        self.stack.append(val)
        
        if not self.min or self.min[-1] >=val:
            self.min.append(val)
     


    def pop(self):
        """
        :rtype: None
        """
        if self.stack and self.min and self.stack[-1]==self.min[-1]:
            self.min.pop()
        if self.stack:
            self.stack.pop()
            
        
        

        

    def top(self):
        """
        :rtype: int
        
        """
        if self.stack:return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        
        if self.min: return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()