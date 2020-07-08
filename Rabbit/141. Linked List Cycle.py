
"""
自解，下面那個是一樣的解法，但寫法更簡潔
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if not head or not head.next or not head.next.next:
            return False
        
        slow = head
        fast = head
        
        while slow.next and fast.next and fast.next.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True

        return False

"""
這裡進了loop 之後先走再比較，所以不會比較兩個head, 就不用像我一樣先init
"""

def hasCycle(self, head):
    fast = head
    slow = head
    # 由於if no cycle, fast一定會先碰到None, 所以只check fast就好! :)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow: 
            return True
    return False

"""
Bridge: 
- 自解，沒那麼漂亮，因為直接init next.next, 所以很多null要check, 但演算法是對的
- 學到了用is來比較objects
"""
def hasCycle(self, head):

    if not head or not head.next or not head.next.next:
        return False
    
    slow = head.next
    fast = head.next.next
    
    while slow and fast:
        if slow is fast:
            return True

        slow = slow.next
        
        if not fast.next:
            return False
        fast = fast.next.next
        
        
    return False