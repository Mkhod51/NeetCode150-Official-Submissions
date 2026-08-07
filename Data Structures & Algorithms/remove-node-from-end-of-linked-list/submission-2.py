# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseLL(head: Optional[ListNode]) -> Optional[ListNode]:
        #reverse 
            prev = None 
            cur = head

            while cur:
                tmp = cur.next 
                cur.next = prev 
                prev = cur 
                cur = tmp 
            
            return prev 
        
        head = reverseLL(head)

        prev = None 
        cur = head 
        counter = 0
        while cur and counter < n - 1:
            counter += 1 
            tmp = cur.next 
            prev = cur 
            cur = tmp 
            
        if n == 1:
            head = head.next
        else: 
            prev.next = cur.next 

        head = reverseLL(head)

        return head 

