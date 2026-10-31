# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Count them 
        cur = head 
        count = 1 

        while cur.next:
            cur = cur.next
            count += 1 

        if count < 2:
            return None
        
        find = count - n + 1
        if find < 2:
            return head.next
        count = 1 
        cur = head 
        
        while count < find - 1:
            cur = cur.next
            count += 1
        
        cur.next = cur.next.next
        return head 

        


