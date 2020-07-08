

"""
algo:
- Viz: 
    - sort first
    - iterate interval list
        - 但在每個interval時都往後check, 直到斷掉
- in-place!
- 先sort是關鍵
- 這裡是in-place去改list, 中途會pop, 所以不能用iterator, 用while然後自己宣告pointer就可以
"""

class Solution(object):
    def merge(self, intervals):

        if intervals is None:
            return
        ls = len(intervals)
        if ls <= 1:
            return intervals


        # sort by start
        intervals.sort(key=lambda x: x.start)
        curr = 0
        while curr < len(intervals) - 1: # "len() - 1", 因為如果是最後一個孤島就沒必要看了
            # 有沒有連起來
            if intervals[curr].end >= intervals[curr + 1].start:
                next = intervals.pop(curr + 1)
                # overlap OR cover
                # cover就不做事，keep curr, next直接pop掉
                if next.end > intervals[curr].end:
                    intervals[curr].end = next.end

            # 斷了，iterate到下一位
            else:
                curr += 1

        return intervals


"""
兔派自解成功
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        curr = 0
        
        while curr < len(intervals) - 1:
            
            
            if intervals[curr][1] >= intervals[curr + 1][0]:
                
                next = intervals.pop(curr + 1)
                if next[1] > intervals[curr][1]:
                    intervals[curr][1] = next[1]
            
            else:
                curr += 1
                
        return intervals