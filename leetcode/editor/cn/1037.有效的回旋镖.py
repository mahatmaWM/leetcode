#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#
# https://leetcode-cn.com/problems/valid-boomerang/description/
#
# algorithms
# Easy (42.37%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 11.7K
# Testcase Example:  '[[1,1],[2,3],[3,2]]'
#
# 回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
#
# 给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
#
#
#
# 示例 1：
#
# 输入：[[1,1],[2,3],[3,2]]
# 输出：true
#
#
# 示例 2：
#
# 输入：[[1,1],[2,2],[3,3]]
# 输出：false
#
#
#
# 提示：
#
#
# points.length == 3
# points[i].length == 2
# 0 <= points[i][j] <= 100
#
#
#
# @lc code=start
class Solution:
    # 三个点各不相同且不在一条直线上
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 判断三个点相同
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]: return False

        # 斜率
        k_1_0, k_2_0 = 'no', 'no'
        if points[1][0] != points[0][0]: k_1_0 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        if points[2][0] != points[0][0]: k_2_0 = (points[2][1] - points[0][1]) / (points[2][0] - points[0][0])

        if k_1_0 == 'no' and k_2_0 == 'no': return False
        if k_1_0 == 'no' or k_2_0 == 'no': return True
        return k_1_0 != k_2_0


# @lc code=end
