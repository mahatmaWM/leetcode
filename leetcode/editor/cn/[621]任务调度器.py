# 给定一个用字符数组表示的 CPU 需要执行的任务列表。
# 其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。
# 任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。
# CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
#
# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。 
#
# 你需要计算完成所有任务所需要的最短时间。 
#
# 示例 1： 
#
# 
# 输入: tasks = ["A","A","A","B","B","B"], n = 2
# 输出: 8
# 执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
# 
#
# 注： 
#
# 
# 任务的总个数为 [1, 10000]。 
# n 的取值范围为 [0, 100]。 
# 
# Related Topics 贪心算法 队列 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import queue
        import collections
        counter = collections.Counter(tasks)
        pq = queue.PriorityQueue(len(counter))
        for k, v in counter.items():
            # print(k,v)
            pq.put((-v, k))
        # print(pq)
        res = 0
        while not pq.empty():
            i = 0
            tmp_list = []
            while i <= n:
                if not pq.empty():
                    item = pq.get()
                    print(item)
                    if item[0] < -1:
                        tmp_list.append((item[0] + 1, item[1]))
                res += 1
                if pq.empty() and not tmp_list:
                    break
                i += 1
            for item in tmp_list:
                pq.put(item)
        return res
        # print(pq.get())


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().leastInterval(
        tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
        n=2))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
