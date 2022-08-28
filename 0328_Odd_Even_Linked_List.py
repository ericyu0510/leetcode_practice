# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_start = ListNode()
        even_start = ListNode()
        odd, even = odd_start, even_start
        cur = head
        odd_flag = True
        while(cur):
            if odd_flag:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
            odd_flag = not odd_flag
        even.next = None
        if even_start.next:
            odd.next = even_start.next
        return odd_start.next