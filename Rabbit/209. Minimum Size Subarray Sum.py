


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



class Solution:
    def minSubArrayLen(self, s, nums) -> int:

        if sum(nums) < s:
            return 0

        ans = float('inf')
        l = 0
        r = 0
        while l < len(nums) and r < len(nums):
            total = sum(nums[l:r + 1])
            if total < s:
                r += 1
            else:
                ans = min(ans, (r - l + 1))

                if ans == 1:
                    return ans

                l += 1

        return ans