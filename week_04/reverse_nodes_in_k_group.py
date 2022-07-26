
"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int) :

        if head is None: return None
        a = b = head
        for i in range(k):
            if b is None: return head
            b = b.next
        res = self.reverse(a ,b)
        a.next = self.reverseKGroup(b ,k)
        return res


    def reverse(self, a, b):
        pre, cur, nxt = ListNode(None), a, a
        while cur is not b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre