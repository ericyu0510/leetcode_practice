# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        dig = 1
        while l1:
            num1 = num1 + l1.val*dig
            l1 = l1.next
            dig *= 10
        dig = 1
        while l2:
            num2 = num2 + l2.val*dig
            l2 = l2.next
            dig *= 10
        num1 = num1+num2
        
        start = ListNode()
        cur = start
        if num1 == 0:
            return start
        while num1 > 0:
            node = ListNode(num1 % 10)
            num1 = num1//10
            cur.next = node
            cur = cur.next
        return start.next