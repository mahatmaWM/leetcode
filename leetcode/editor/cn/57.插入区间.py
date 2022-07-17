#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (37.25%)
# Likes:    151
# Dislikes: 0
# Total Accepted:    23.7K
# Total Submissions: 63.5K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
#
#
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#
#


# @lc code=start
class Solution:
    # 原始有序，insert到合适位置，然后采用类似56题思路合并区间
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_index = len(intervals)
        for i, it in enumerate(intervals):
            if it[0] > newInterval[0]:
                insert_index = i
                break
        intervals.insert(insert_index, newInterval)

        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            # 如果curr的end比新的start小，则保存一个结果，更新curr
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            else:
                # 更新curr的end值
                curr[1] = max(intervals[i][1], curr[1])
        res.append(curr)
        return res


# @lc code=end
