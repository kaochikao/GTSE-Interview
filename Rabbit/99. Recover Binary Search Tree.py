
"""
- 這個解法只有解到一半，只work when 需要swap的是連續的

   1
  /
 3
  \
   2

- 以上圖為例，此解能正確in-order traverse [3->2->1]
- 但最後output是 [2->3->1], 因為看到2就以為錯了，就swap了，但正解應該要是1,3 swap.
"""
class Solution(object): # first, self-attempt
    def recoverTree(self, root):
        stack = []
        prev = TreeNode(val=float('-inf'))

        while root or stack:
            
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            if root.val < prev.val:                
                prev.val, root.val = root.val, prev.val
                break
            
            prev = root
            root = root.right


# Solution: https://github.com/qiyuangong/leetcode/blob/master/python/099_Recover_Binary_Search_Tree.py