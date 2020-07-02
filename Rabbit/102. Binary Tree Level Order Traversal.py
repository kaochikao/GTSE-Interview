

"""
Algo:
- 由於recursion想起來一定要先不斷left下去，所以用iteration.

實現：
- 用新學的deque & 2個queue的技巧實現成功
"""
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        ans = []
        q = deque([root])
        
        while q: 
            
            layer = []
            new_q = deque([])
            while q:
                node = q.popleft()
                layer.append(node.val)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                
            q = new_q
            ans.append(layer)
        
        return ans

# 方法2：紀錄depth
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        
        def rec(node, depth, memo):
            
            if not node:
                return
            
            if depth in memo:
                memo[depth].append(node.val)
            else:
                memo[depth] = [node.val]
            
            rec(node.left, depth + 1, memo)
            rec(node.right, depth + 1, memo)
        
        ans = []
        M = {}
        rec(root, 0, M)
        
        for k in M:
            ans.append(M[k])
            
        return ans


"""
From Answer
- 此法等於是結合我上面兩種方式
- 他用iteration, 但不把整層遍歷玩，而是紀錄depth.
- 實現上，用2D array當dict的技巧蠻有趣的
"""
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        ans = []

        if not root: 
            return ans

        q = deque()
        q.append((root, 0))

        while q:
            node, depth = q.popleft()
            if depth < len(ans):
                # interesting :)
                ans[depth].append(node.val)
            else:
                ans.append([node.val])
            if node.left: 
                q.append((node.left, depth + 1))
            if node.right: 
                q.append((node.right, depth + 1))
        return ans