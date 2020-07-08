
"""
自解recursive
"""

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:    
    
        if not root:
            return False
        
        sum -= root.val
        
        if not root.left and not root.right:
            if sum == 0:
                return True
            else:
                return False
            
        l = r = False
        if root.left:
            l = self.hasPathSum(root.left, sum)
        
        if root.right and not l:
            r = self.hasPathSum(root.right, sum)
            
        return l or r

"""
把上面的code簡化 = Ans
"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:    
    
        if not root:
            return False
        
        sum -= root.val
        
        if not root.left and not root.right and sum == 0:
            return True

        l = self.hasPathSum(root.left, sum)
        r = self.hasPathSum(root.right, sum)
            
        return l or r