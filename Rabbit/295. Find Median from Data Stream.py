
"""
Ans: https://blog.csdn.net/u013832707/java/article/details/103488414

algo:
- maintain 2 heaps
- min heap contains the larger half
- max heap contains the smaller half
- minh 最多比maxh 多一個element
- median = (minh top) OR (avg of both top)

實現：
- 由於python heapq只支援min heap, 所以這裡任何放到maxh的element都以其負值放入
"""
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxh = []
        self.minh = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        if self.length == 1:
            heapq.heappush(self.minh, num)
            return
        
        if num >= self.minh[0]:
            heapq.heappush(self.minh, num)
            if len(self.minh) > len(self.maxh) + 1:
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))
        else:
            heapq.heappush(self.maxh, -num)
            if len(self.minh) < len(self.maxh):
                heapq.heappush(self.minh, -heapq.heappop(self.maxh))
        

    def findMedian(self) -> float:
        if self.length % 2:
            return self.minh[0]
        else:
            return (self.minh[0] + -self.maxh[0]) / 2
