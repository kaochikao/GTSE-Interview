

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


"""
Ans:

- 這裡dummy head不是為了建另一個linked list, 只是加個prev, 這裡還是in-place在swap.
"""
class Solution(object):
    def swapPairs(self, head):
        dummyHead = ListNode(-1)
        dummyHead.next = head
        prev, p = dummyHead, head

        while p and p.next:
            q, r = p.next, p.next.next


            # swap 2 nodes 其實有3個 "links"需要改
            prev.next = q
            q.next = p
            p.next = r

            prev = p
            p = r

        return dummyHead.next