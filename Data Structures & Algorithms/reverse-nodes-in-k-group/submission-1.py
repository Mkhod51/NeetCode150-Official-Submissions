# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLL(head, k):
            prev = None 
            cur = head 
            explore = head
            for i in range(k):
                if not explore:
                    return [head, None, False] 
                explore = explore.next 
                
            for i in range(k):
                tmp = cur.next 
                cur.next = prev 
                prev = cur 
                cur = tmp

            
            return [prev, cur, True]
        
        dummy = ListNode()
        tail = dummy 
        cur = head 

        while cur:
            curHead, nextHead, status = reverseLL(cur, k)

            if not status:
                tail.next = cur 
                break
            
            tail.next = curHead
            tail = cur 
            cur = nextHead

        return dummy.next


