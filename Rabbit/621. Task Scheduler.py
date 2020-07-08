class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks = building a map
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        
        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)



https://github.com/wuduhren/leetcode-python/blob/master/problems/task-scheduler.py
class Solution(object):
    def leastInterval(self, tasks, n):
        task_count = collections.Counter(tasks).values()

        # 一樣是先求max frequency
        max_count = max(task_count) #[2]
        t = task_count.count(max_count) #[1]
        return max(len(tasks), (max_count-1)*(n+1)+t) #[3]
