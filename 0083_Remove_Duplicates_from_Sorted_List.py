# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        last = head
        prev = head
        cur = head.next
        while(cur):
            if cur.val == prev.val:
                prev = cur
                cur = cur.next
                last.next = cur
                
            else:
                prev = cur
                cur = cur.next
                last = prev
        return head