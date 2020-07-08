
"""
algo:
- 直接從total可以取得一些資訊
- 不用考慮要找到兩種能組成target的組合，因為已經除2了，代表只要有一組”剛好“等於target, 另外一半就一定是

思路：
- 用given elements是否能達到target sum.
- 求TOTAL是否能被組成
- num1是否能跟其他element組成TOTAL = "TOTAL - num1" 是否能被組成
- (((TOTOAL - num1) - num2) - num3) ... 是否能被組成


"""

# [1,5,11,5]

class Solution(object):


    def canPartition(self, nums):
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:

            # 從target一路-1減到num本身
            # foreach num, 都會從 i = target開始，因為這就是目的
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

                # 加入這個check可以提前結束
                if dp[target]:
                    return True

        return dp[target]

""" 
evolution:

100000000000 -> 0
110000000000 -> 1   (num: 1, i: 1)
110000100000 -> 6   (num: 5, i: 6)
110001100000 -> 5   (num: 5, i: 5)
110001100001 -> 11  (num: 11, i: 11)
110001100011 -> 10  (num: 5, i: 10)
"""

"""
速度：(前面找很久，後面找很快)
100000000000
100000000000
100000000000
100000000000
100000000000
100000000000
100000000000
100000000000
100000000000
100000000000

110000000000
110000000000
110000000000
110000000000
110000000000
110000000000

110000100000

110001100000

110001100001
110001100001

110001100011
110001100011
110001100011
110001100011
110001100011
110001100011
"""
