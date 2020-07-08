

# 二刷自解
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.d = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz',
                '0': ' '}
        
        self.digits = digits
        
        if len(digits) == 0:
            return []
        
        tmp = [x for x in self.d[digits[0]]]
        return self.rec(tmp, 1)
        
        
    def rec(self, a, p):
        
        
        if p == len(self.digits):
            return a
        
        new_a = []
        
        for i in a:
            for j in self.d[self.digits[p]]:
                
                new_a.append(i + j)
                
        return self.rec(new_a, p + 1)

"""
自解 recursion, BFS
其實我做的好像也是DFS?!
這題是combination, not permutation
"""
class Solution(object):
    def letterCombinations(self, digits):

        if len(digits) == 0:
            return []

        dmap = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz',
                '0': ' '}

        return self.rec(digits, 0, dmap, '')
        
            


    def rec(self, digits, curr, dmap, sb):
        # detail, 如果我這裡不是用string buffer, 而是用list, 上面就不用check edge case.
        if curr == len(digits):
            return [sb]

        tmp_l = []
        for c in dmap[digits[curr]]:
            tmp = self.rec(digits, curr + 1, dmap, sb + c)
            tmp_l.extend(tmp)

        return tmp_l

    
# 自解 brute force
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        dmap = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz',
                '0': ' ',
                None: None}
        
        prev = [c for c in dmap[digits[0]]]
        
        for i in range(1, len(digits)):
            
            curr = []
            for c in prev:
                for k in dmap[digits[i]]:
                    curr.append(c + k)
                    
                    
            prev = curr
            
        return prev

"""
algo:
- answer, DFS
- BFS = 把一個digit的所有possibility都

實現：
- 這裡回傳回來的"result"是用名為posfix的variable存著，本層return時是另外宣告另一個result = [], 所以不用想要怎麼把下層除回來的result "transform"成往上層傳的result
"""
class Solution(object):
    def letterCombinations(self, digits):

        result = []
        ls = len(digits)
        if ls == 0:
            return result
        current = digits[0]
        posfix = self.letterCombinations(digits[1:])
        # 這裡return回來的posfix其實就是result
        # 下面可以看到nested for loop, 就是 dmap[current] * posfix

        for t in dmap[current]:
            if len(posfix) > 0:
                for p in posfix:
                    # 因為是走到底再彈回來，所以t是prepend (加在前面)
                    temp = t + p
                    result.append(temp)
            else:
                result.append(t)

        return result
