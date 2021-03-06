#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#
# https://leetcode-cn.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (58.51%)
# Likes:    82
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 29.6K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
#
# （这里，平面上两点之间的距离是欧几里德距离。）
#
# 你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
#
#
#
# 示例 1：
#
# 输入：points = [[1,3],[-2,2]], K = 1
# 输出：[[-2,2]]
# 解释：
# (1, 3) 和原点之间的距离为 sqrt(10)，
# (-2, 2) 和原点之间的距离为 sqrt(8)，
# 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
# 我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
#
#
# 示例 2：
#
# 输入：points = [[3,3],[5,-1],[-2,4]], K = 2
# 输出：[[3,3],[-2,4]]
# （答案 [[-2,4],[3,3]] 也会被接受。）
#
#
#
#
# 提示：
#
#
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
#
#

# @lc code=start
import heapq
import math


class Solution:
    # 首先把每个元素距离原点的距离和该坐标组成tuple放到list里面，这样构建堆的时候，会按照第一个元素自动排序。
    # 提供了nsmallest方法直接取出最小的K个tuple，然后把坐标返回即可。
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = []
        for p in points:
            d = math.sqrt(p[0]**2 + p[1]**2)
            dis.append((d, p))
        heapq.heapify(dis)
        return [d[1] for d in heapq.nsmallest(K, dis)]


# @lc code=end
