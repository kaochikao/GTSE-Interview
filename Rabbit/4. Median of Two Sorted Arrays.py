class Solution(object):
    def findMedianSortedArrays(self, X, Y):
        if len(X)>len(Y): 
            X, Y = Y, X

        # X & M 是長的
        M, N = len(X), len(Y)

        after = (M+N-1)/2
        l, h = 0, M

        while l<h:
            i = (l+h)/2
            if after-i-1 < 0 or X[i] >= Y[after-i-1]:
                h = i
            else:
                l = i + 1
        i = l
        nextfew = sorted(X[i:i+2] + Y[after-i:after-i+2])
        return (nextfew[0]+nextfew[1-(M+N)%2])/2.0

# https://www.youtube.com/watch?v=ScCg9v921ns (很好的解釋)
def findMedianSortedArrays(self, nums1, nums2):
    # https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation
    # https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation
    ls1, ls2 = len(nums1), len(nums2)
    if ls1 < ls2:
        return self.findMedianSortedArrays(nums2, nums1)

    # nums1 是長的
    l = 0
    r = ls2 * 2 # 短的2倍

    while l <= r:
        mid2 = (l + r) // 2
        mid1 = ls1 + ls2 - mid2

        if mid1 == 0:
            L1 = float('-inf')
        else:
            L1 = nums1[(mid1 - 1) // 2]

        if mid2 == 0:
            L2 = float('-inf')
        else:
            L2 = nums2[(mid2 - 1) // 2]

        if mid1 == 2 * ls1:
            R1 = float('inf')
        else:
            R1 = nums1[mid1 // 2]

        if mid2 == 2 * ls2:
            R2 = float('inf')
        else:
            R2 = nums2[mid2 // 2]


        if L1 > R2:
            l = mid2 + 1
        elif L2 > R1:
            r = mid2 - 1
        else:
            return (max(L1, L2) + min(R1, R2)) / 2.0