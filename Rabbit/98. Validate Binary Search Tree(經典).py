

# BST 不是只是在小樹中 parent > left, parent < right. 還要看整個tree, 大的都要在右邊，小的都在左邊．

"""

Bridge: 
- 解了幾次，看過答案後終於解成功，直得review, 多想幾次．

Algo理解：
- 要check 2 件事，left val一定要小於parent & root, 但根本不用check是否小於root, 因為parent已經小於root.
- 左邊要check max, 右邊要check min, 若要用同樣的function, 就要有這兩個args, 但可以用inf & -inf, 讓結果不被影響

實現：
- 由於BST不能有duplicate key, 所以任何check 都要用<= or >=
- again, edge case 沒考慮到，tree的edge case就是root是None

"""
# 

class Solution(object):
    def isValidBST(self, root):
        return self.rec(root, float('-inf'), float('inf'))

    def rec(self, node, min_val, max_val):

        if node is None:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        l = self.rec(node.left, min_val, node.val)
        r = self.rec(node.right, node.val, max_val)

        return l and r


# in-order

"""
- in-order 解法
- 由左到右
- 初始stack就是左線
- root要想成pointer
"""

"""
stack 變化
[8, 3, 1]
[8, 3]
[8, 6, 4]
[8, 6]
[8, 7]
[8]
[10]
[14, 13]
[14]
"""

"""
traverse方式：
- 1->3: right is None, 所以切回去看stack
- 3->4: 有right (6), 這個right又會把左線加入stack
- 6->7: 本身自己check完就會去看right
"""

def isValidBST(self, root):

    stack = []
    last_val = float('-inf')

    while root or stack:

        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if root.val <= last_val:
            return False

        last_val = root.val
        root = root.right
        # if right is None, 則while loop從root切到stack, 也就是左線 
    return True



# iteration & stack
def isValidBST(self, root):
    if not root:
        return True
    stack = [(root, float('-inf'), float('inf'))]

    while stack:

        node, min_val, max_val = stack.pop()

        if node.val <= min_val or node.val >= max_val:
            return False

        if node.left:
            stack.append((node.left, min_val, node.val))
        if node.right:
            stack.append((node.right, node.val, max_val))

    return True

# ------------------------------------------------------------------------------------------------------------

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n4 = TreeNode(val=4)
n7 = TreeNode(val=7)
n13 = TreeNode(val=13)

n1 = TreeNode(val=1)
n6 = TreeNode(val=6, left=n4, right=n7)
n14 = TreeNode(val=14, left=n13)

n10 = TreeNode(val=10, right=n14)
n3 = TreeNode(val=3, left=n1, right=n6)

n8 = TreeNode(val=8, left=n3, right=n10)

s = Solution()
s.isValidBST(n8)