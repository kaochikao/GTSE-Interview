"""
iteration解法
- time: linear
- space: linear

achievement:
- 現用了剛學到的stack.
- 用兩個while loop來分解，不像以前會很僵硬想要one-shot
"""

class Solution(object):
    def reverseList(self, head):

        if not head:
            return head
        
        stack = []
        
        while head:
            stack.append(head.val)
            head = head.next
            
        ans_head = ListNode(stack.pop())
        curr = ans_head
        
        while stack:
            
            tmp_node = ListNode(val=stack.pop())
            curr.next = tmp_node
            curr = tmp_node
            
        return ans_head


"""
iteration & constant space
- 其實所謂reverse, 就是swap所有pointers. 但仔細一想，只有一個next pointer, prev在前一個node上
    - 其實沒有要swap前一個pointer, 只要換next就好
- 原本擔心換了pointer就無法traverse, 但其實先存下來就可
"""

def reverseList(self, head):

    prev = None
    while head:
        
        tmp_next = head.next
        head.next = prev

        prev = head
        head = tmp_next

    return prev




"""
Recursive
- 先traverse, 到最後一個的時候會反彈，回來後變"new_head"
- 實際swapping從倒數第二個開始，把下個node的next pointer指到自己，並把自己到next的pointer斷開
- 由於各recursion stack的local var就有該stack當下的state, 所以swap時完全不用存tmp pointer.
"""

# 1->2->3->4->5->NULL
def reverseList(self, node):
    if node and node.next:
        # 這個new head其實永遠都是5, 各stack都沒用到這個return value, 只用node, which is local to the stack.
        new_head = self.reverseList(node.next)
        node.next.next = node
        node.next = None
        return new_head
    
    # 只有5用到這個return
    return node