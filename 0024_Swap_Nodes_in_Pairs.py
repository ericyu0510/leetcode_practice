# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if head and head.next:
            head = head.next
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            prev = cur
            cur = cur.next
        while(cur and cur.next):
            prev.next = cur.next
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            prev = cur
            cur = cur.next
        return head