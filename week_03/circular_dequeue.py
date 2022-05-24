'''
Design your implementation of the circular double-ended queue (deque).
Implement the MyCircularDeque class:
MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.

Example 1:
Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]
Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
'''

class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.queue.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.queue[0]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.queue

    def isFull(self) -> bool:
        return len(self.queue) == self.k

# Your MyCircularDeque object will be instantiated and called as such:
if __name__ == '__main__':
    k=10

    obj = MyCircularDeque(k)
    param_1 = obj.insertFront(1)
    param_2 = obj.insertLast(2)
    # param_3 = obj.deleteFront()
    # param_4 = obj.deleteLast()
    param_5 = obj.getFront()
    param_6 = obj.getRear()
    param_7 = obj.isEmpty()
    param_8 = obj.isFull()
    print(param_1)
    print(param_2)
    # print(param_3)
    # print(param_4)
    print(param_5)
    print(param_6)
    print(param_7)
    print(param_8)

