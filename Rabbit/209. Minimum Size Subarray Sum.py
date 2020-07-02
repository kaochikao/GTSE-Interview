


# https://blog.csdn.net/fuxuemingzhu/article/details/83063096
class Solution:
    def minSubArrayLen(self, s, nums):

        l, r = 0, 0
        csum = 0
        res = float('inf')
        while r < len(nums):
            csum += nums[r]
            while csum >= s:
                res = min(res, r - l + 1)
                csum -= nums[l]
                l += 1
            r += 1

        if res != float('inf'):
            return res
        else:
            return 0

