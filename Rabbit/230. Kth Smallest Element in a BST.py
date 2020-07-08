

"""
自解，秒解，in-order traversal
我做的這個就是 Iterative in-order traversal
"""

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        i = 0
        stack = []
        
        while stack or root:
            while root:
                
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            
            i += 1
            if i == k:
                return root.val
        
            root = root.right


"""
Ans, Rec in-order
"""

class Solution:
    def kthSmallest(self, root, k):

        def inorder(r):
            # 這裡加的順序就是in-order
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]


