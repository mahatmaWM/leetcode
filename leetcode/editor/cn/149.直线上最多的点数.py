#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode-cn.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (22.31%)
# Likes:    148
# Dislikes: 0
# Total Accepted:    12.6K
# Total Submissions: 56.7K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
#
# 示例 1:
#
# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o
# +------------->
# 0  1  2  3  4
#
#
# 示例 2:
#
# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#


# @lc code=start
class Solution:
    # 两次遍历节点，分别计算斜率计数
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3: return len(points)

        # 获取i点到j点的斜率（i点在j点右边），排除小数精度的影响，结果用最简分数表示
        def getSlope(point_i, point_j):
            if point_i[0] < point_j[0]: return getSlope(point_j, point_i)
            d_x = point_j[0] - point_i[0]
            d_y = point_j[1] - point_i[1]
            if d_x == 0: return (0, point_i[0])
            if d_y == 0: return (point_i[1], 0)
            tmp = math.gcd(d_x, d_y)
            return (d_y // tmp, d_x // tmp)

        ans = 0
        for i in range(len(points)):
            curr_cnt = collections.defaultdict(int)
            same_points = 1
            point_i = points[i]
            curr_max = 0
            for j in range(i + 1, len(points)):
                point_j = points[j]
                if point_i == point_j:
                    same_points += 1
                else:
                    slope = getSlope(point_i, point_j)
                    curr_cnt[slope] += 1
                    curr_max = max(curr_max, curr_cnt[slope])
                    # print('slope={},p1={},p2={},curr_cnt={}'.format(slope, point_i, point_j, curr_cnt))
            # 注意加上本轮重复的点
            ans = max(ans, same_points + curr_max)
        return ans


# @lc code=end
