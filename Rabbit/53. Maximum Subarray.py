
"""
自解

algo:
- 這題屬於DP

DP: 
Dynamic Programming中文譯作動態規劃，動態規劃類似Divide and Conquer，一個問題的答案來相依於子問題，常用來解決最佳解的問題。
與Divide and Conquer不同的地方在於，動態規劃多使用了memoization的機制，將處理過的子問題答案記錄下來，避免重複計算，因此在子問題重疊的時候應該使用動態規劃；
Divide and Conquer通常使用遞迴(Top-Down)來處理，轉成迭代法(Bottom-up)來解並不容易，故使用動態規劃則可以解決重覆計算並保留遞迴思考的優點。

Fibonacci就是一個例子
"""

class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        A = [0] * len(nums)
        A[0] = nums[0]

        for i in range(1, len(nums)):
            # key: 我要不要帶著prefix, 還是我自己當頭
            A[i] = max(nums[i], A[i - 1] + nums[i])

        return max(A) # key, 不是return A[-1]


"""
[0]
if we know the max value of the subarray that ends at i index is Mi
what is the max value of the subarray that ends at i+1 index?
its either nums[i+1] or nums[i+1]+Mi
so code below, maxCurrent[i] stores the max value of subarray that ends at i
[1]
the max value of the subarray that ends at 0, has to be nums[0].
[2]
the max value of subarray must ends in one of the index of nums
so we get the max(maxCurrent).
"""

# [-2,1,-3,4,-1,2,1,-5,4]

class Solution(object):
    def maxSubArray(self, nums):

        if nums==None or len(nums)==0: 
            return None

        maxCurrent = [nums[0]] #[1]

        for i in xrange(1, len(nums)):
            maxCurrent.append(max(nums[i], nums[i]+maxCurrent[-1])) #[0]
        return max(maxCurrent) #[2]



class Solution(object):
    def maxSubArray(self, nums):

        if not nums: 
            return 0

        cur, prev = 0, 0
        res = float("-inf")
        for i in range(len(nums)):
            cur = nums[i] + (prev if prev > 0 else 0)
            prev = cur
            res = max(res, cur)
        return res


# pattern: first & last item of the sub-array is never going to be negative
# edge case: all negative items -> sum = 0 = 0 length sub-array




class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        A = [0] * len(nums)
        A[0] = nums[0]

        for i in range(1, len(nums)):
            A[i] = max(nums[i], A[i - 1] + nums[i])

        return max(A)