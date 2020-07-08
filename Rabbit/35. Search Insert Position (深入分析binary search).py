


"""
標準正解
"""
        
class Solution(object):
    def searchInsert(self, nums, target):

        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l


# 自己寫的錯誤解, inf loop，下面有深度分析3個topics
class Solution:
    def searchInsert(self, nums, target) -> int:

        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid #wrong, should be "mid + 1"
                
        return l

"""
Binary Search的問題：
1. [DONE] mid計算：記得加left
2. [WIP] pointer走法, 要collapse
3. [TODO] right要用len(nums) OR len(nums) - 1?
"""

# topic 1: mid 
"""
- 原本用 mid = (r - l) // 2 但因為example是一直往左，所以沒看出錯誤
- 應該要要把l加上去 --> mid = l + (r - l) // 2
"""

# topic 2: pointer
"""
範例1：
[1, 3, 5, 6]

- 找2, 卡在 0-0-1
- 找4, 卡在 1-1-2
- 找7, 卡在 3-3-4

範例2：
[1, 3, 5, 6, 10, 20, 32, 45, 65]

- 找34, 卡在 6-6-7 = 32

錯誤在於"l = mid", 因為取//, 所以mid不是真的mid, 會降一格，回到自己
所以當"l = mid", 代表下個iteration的state是一樣的 --> inf loop --> never collapse
一開始的大距離收斂沒問題，縮到已經到隔壁時就collapse不了

基數偶數長度似乎無關，總是會收斂到剩兩個，也就是偶數，在偶數情況下取mid就會有這種降一格的情況
"""

# topic 3: en(nums) || len(nums) - 1?

"""
範例：
[1, 3, 5, 6]

- 找7, 會找不到，因為一開始的6就是end, 永遠不會往右走，左邊沒這個問題，因為//會降回自己
"""


# another solution
"""
- 這裡mid算法是相加，所以不用加left
- 注意兩個key, 其他都一樣

範例：
[1, 3, 5, 6]

- 找7, index out of range
- 這裡一開始不能是“len(nums)”，因為最終left會收斂到right = len(nums), 因為一開始沒有”exclude“掉

"""
class Solution:
    def searchInsert(self, nums, target):

        l = 0
        r = len(nums) - 1 # key, cannot be len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target: 
                l = mid + 1
            else:
                r = mid
        
        # key
        if nums[l] < target: 
            return l + 1
        return l

# 小改exercise (modify the above solution)
"""
把上面的小改一下就可以了
"""
class Solution:
    def searchInsert(self, nums, target):

        l = 0
        r = len(nums) # key

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target: 
                l = mid + 1
            else:
                r = mid
        
        # key
        if l == len(nums):
            return len(nums)
        
        if nums[l] < target:
            return l + 1
        return l