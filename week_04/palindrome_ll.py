
"""
Given the head of a singly linked list, return true if it is a palindrome.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        def reverseList(head: ListNode) -> ListNode:
          prev = None
          curr = head

          while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

          return prev

        slow = head
        fast = head

        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next

        if fast:
          slow = slow.next
        slow = reverseList(slow)

        while slow:
          if slow.val != head.val:
            return False
          slow = slow.next
          head = head.next

        return True

