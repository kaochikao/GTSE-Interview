class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        
        while root or stack:
            
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            ans.append(root.val)
            
            root = root.right
        
        return ans


        
# 

"""
Recursive法做in-order:
- 要想像leaf node之下還有left & right兩個隱形nodes, 用來回彈．
- 左邊彈回來後，記錄“自己”，並traverse右邊，不直接紀錄右邊，因為他自己也會終究到自己的層去記錄自己．
- 理解key: 這裡是紀錄“自己”，不是紀錄左node. 關鍵在於timing, 在traverse完left後記錄自己，然後traverse右邊，就這樣．
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def rec(node, ans):
            if not node:
                return
            
            rec(node.left, ans)
            ans.append(node.val)
            rec(node.right, ans)
            return
        
        A = []
        rec(root, A)
        return A