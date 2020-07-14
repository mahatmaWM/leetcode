#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
# https://leetcode-cn.com/problems/task-scheduler/description/
#
# algorithms
# Medium (49.37%)
# Likes:    289
# Dislikes: 0
# Total Accepted:    24.2K
# Total Submissions: 49K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26
# 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
#
# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
#
# 你需要计算完成所有任务所需要的最短时间。
#
#
#
# 示例 ：
#
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
# ⁠    在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
#
#
#
# 提示：
#
#
# 任务的总个数为 [1, 10000]。
# n 的取值范围为 [0, 100]。
#
#
#

# @lc code=start
class Solution1:
    # 使用优先队列模拟整个过程，会超时
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)

        # 优先队列，根据任务多少排序(优先级取负)
        pq = queue.PriorityQueue(len(counter))
        for k, v in counter.items():
            pq.put((-v, k))
            
        res = 0
        while not pq.empty():
            i = 0
            tmp_list = []
            # 根据优先级高低取出n+1个任务，然后更新后再次入队列
            while i <= n:
                if not pq.empty():
                    item = pq.get()
                    if item[0] < -1: tmp_list.append((item[0] + 1, item[1]))
                res += 1
                if pq.empty() and not tmp_list: break
                i += 1
            for item in tmp_list:
                pq.put(item)
        return res

class Solution:
    # 贪心的思路，(出现的次数最多的 - 1) * (n + 1) + (出现的次数最多的任务 的个数)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1: return length

        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)

        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)

        for sort in task_sort:
            if sort[1] == max_task_count: res += 1

        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length
# @lc code=end

