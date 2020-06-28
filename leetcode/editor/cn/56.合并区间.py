#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (42.68%)
# Likes:    459
# Dislikes: 0
# Total Accepted:    104.9K
# Total Submissions: 245.8K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])

        curr = intervals[0]
        for i in range(1, len(intervals)):
            # 如果curr的end比新的start小，则保存一个结果，更新curr
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            # 更新curr的end值
            else:
                curr[1] = max(intervals[i][1], curr[1])
        res.append(curr)
        return res
# @lc code=end

