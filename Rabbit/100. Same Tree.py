

"""
algo不難，實現一開始有出錯
- 下方comment處，原本是直接return, 但應該要左右合併結果 l and r

"""

def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    
    # edge case
    if not p and not q:
        return True
    elif not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    if p.left and q.left:  
        l = self.isSameTree(p.left, q.left)
    elif not p.left and not q.left:
        l = True
        # return True
    else:
        l = False
        # return False

    if p.right and q.right:  
        r = self.isSameTree(p.right, q.right)
    elif not p.right and not q.right:
        r = True
        # return True
    else:
        r = False
        # return False
    
    return l and r


"""
Algo:
- 用iteration法去traverse tree其實就是用一個data structure去存，然後不斷把children存進去，直到data structure空掉．

- 此題測試過用stack也行，但確實用queue比較合理，root先看到就先check
- 用2個queue的方式很不錯．

"""

from collections import deque

def isSameTree(self, p, q):
    q1 = deque([p])
    q2 = deque([q])
    while q1 or q2:

        # 這裡一開始看很不直觀，想一下蠻有趣的，(q1 or q2)滿足了才會進來
        if not q1 or not q2: 
            return False
        n1 = q1.popleft()
        n2 = q2.popleft()
        
        if n1 and n2:
            if n1.val!=n2.val: 
                return False
            q1.append(n1.left)
            q1.append(n1.right)
            q2.append(n2.left)
            q2.append(n2.right)
        elif n1 and not n2:
            return False
        elif not n1 and n2:
            return False
    return True


