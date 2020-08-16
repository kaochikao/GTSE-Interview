

# 2刷自解
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.A = []
        self.rec("", n, n)
        return self.A
        
    def rec(self, path, l, r):
        
        if l == 0 and r == 0:
            self.A.append(path)
            return 
            
        if l > r:
            return 
        
        if l == 0:
            self.A.append(path + ")" * r)
            return 
        
        self.rec(path + "(", l - 1, r)
        self.rec(path + ")", l, r - 1)

"""
limit: #) >= #(
remaining

n = 3
["((()))","(()())","(())()","()(())","()()()"]

這是DFS, viz就是一個 binary tree = 加左或加右
會一路先狂加左, 所以第一個答案是((()))

"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        A = []
        L = n
        R = n
        self.rec(L, R, '', A)
        return A
        
    
    def rec(self, l, r, sb, ans):
        if r < l:
            return
        
        if l == 0 and r == 0:
            ans.append(sb)
            return
        elif l == 0:
            # flush
            ans.append(sb + ')'*r)
            return
        

        
        self.rec(l - 1, r, sb + '(', ans)
        self.rec(l, r - 1, sb + ')', ans)