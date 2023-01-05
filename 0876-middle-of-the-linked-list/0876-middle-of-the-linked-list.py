# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        
        count=0
        
        while node:
            node= node.next
            count+=1
        print(count)
        
        hd= head
        
        for i in range(1, count):
            if i == count//2:
                return hd.next
            else:
                hd= hd.next
        return head
            
            
        