# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None
        less = ListNode()
        less_start = less
        greater = ListNode()
        greater_start = greater
        cur = head
        while(cur):
            if cur.val < x:
                less.next = cur
                less = less.next
                cur = cur.next
            else:
                greater.next = cur
                greater = greater.next
                cur = cur.next
        if greater_start.next:
            greater.next = None
        if less_start.next:
            less.next = greater_start.next
            return less_start.next
        else:
            return greater_start.next