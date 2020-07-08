
# ans
# https://blog.csdn.net/fuxuemingzhu/java/article/details/79254648


"""
Example: x = 90

while loop 最後一個iteration會是
- left: 9
- right: 10
- mid: 9

此時，9**2 = 81 還是小於 90, 所以left還會往右走
下次要進loop, 因為超過，就break了，所以要left - 1退一格
"""
class Solution(object):
    def mySqrt(self, x):

        left, right = 0, x + 1

        # 如何收斂？
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid

        # why?
        return left - 1
