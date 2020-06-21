

"""
Bridge: 自解成功, 但一開始沒考慮到edge case.

理解：
- Linked List edge case就一定會有空的head.
"""
class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head

        head_p = head
        curr = head
        while True:
            if not curr.next:
                break
            else:
                curr.val, curr.next.val = curr.next.val, curr.val

            if not curr.next.next:
                break
            else:
                curr = curr.next.next

        return head_p