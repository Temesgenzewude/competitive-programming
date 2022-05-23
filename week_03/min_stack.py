'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.


Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''

class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            val=self.stack.pop()
            self.stack.append(val)
            return val

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            min=self.top()
            for i in range(len(self.stack)):
                if min> self.stack[i]:
                    min=self.stack[i]
            return min



# Your MinStack object will be instantiated and called as such:

def main():
    val=3
    obj = MinStack()
    obj.push(val)
    obj.pop()
    obj.push(6)
    obj.push(7)
    obj.push(8)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)
main()
