"""
Bridge: 目前實作失敗

理解：關於carry, 如果最後是999999, 就比較麻煩

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class Solution(object):
    def addTwoNumbers(self, L1, L2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def rec(l1, l2, carry):
            curr = l1.val + l2.val + carry
            if curr > 9:
                carry = curr / 10
                curr = curr % 10
            else:
                carry = 0
            l1.val = curr

            if l1.next and l2.next:
                rec(l1.next, l2.next, carry)
            elif l1.next and not l2.next:
                if carry > 0:
                    l1.next.val += carry
                return
            elif not l1.next and l2.next:
                l1.next = l2.next
                l2.next.val += carry
                return
            else:
                if carry > 0:
                    l1.next = ListNode(val=carry)
                return

        root = L1
        rec(L1, L2, 0)
        return root



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        # dummy head
        head = curr = ListNode(0)

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = val / 10
        if carry > 0:
            curr.next = ListNode(carry)
            
        return head.next