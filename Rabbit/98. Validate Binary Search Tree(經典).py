

# BST 不是只是在小樹中 parent > left, parent < right. 還要看整個tree, 大的都要在右邊，小的都在左邊．

"""

Bridge: 
- 解了幾次，看過答案後終於姐成功，直得review, 多想幾次．

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