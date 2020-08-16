# 二刷自解
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.nums = nums
        self.A = []
        
        self.rec([], nums)
        return self.A
        
    def rec(self, path, options):
        
        if len(path) == len(self.nums):
            self.A.append(path)
            return
        
        for i in range(len(options)):

            self.rec(path + [options[i]], options[:i] + options[i+1:])


"""

input:  [1,2,3]
output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

從最後一位開始替換，所以是DFS

[1,2,3] --> [1,3,2]
- 這時第3位已經無法替換，所以換第二位為3, 第三位理所當然只剩2這個選項

[1,3,2] --> [2,1,3]
- 這時由於第二位已換完，所以去iterate第一位
- 第一位從1 step到2
- 第二位從1開始

[2,1,3] --> [2,3,1]
- 這裡就可以看到是第二位在iterate

看output的順序就可以知道flow, 第一個recursion stack到底就是完成了[1, 2, 3]
回來之後，for loop繼續，但注意，這時候還沒彈回最上層，所以是去iterate第二位
"""

class Solution(object):
    def permute(self, nums):
        def dfs(path, options):
            print(options)
            if len(nums)==len(path):
                opt.append(path)
                return
            for i, num in enumerate(options):
                dfs(path+[num], options[:i]+options[i+1:])

        opt = []
        dfs([], nums)
        return opt

"""
print(options)的output


[1, 2, 3]       #一路往下
[2, 3]          #一路往下
[3]             #一路往下
[]              # 完成第一個答案之後彈回上層
for end         # for end 其實也往上return 一層．既然往上，iterator就會走，這時第二位已經走到3了，所以在path已經是[1,3]的情況下，往下層走，options剩[2]
[2]
[]
for end
for end
[1, 3]
[3]
[]
for end
[1]
[]
for end
for end
[1, 2]
[2]
[]
for end
[1]
[]
for end
for end
for end
"""