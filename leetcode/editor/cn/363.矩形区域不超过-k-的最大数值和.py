#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#
# https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (36.41%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 10.3K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# 给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。
#
# 示例:
#
# 输入: matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出: 2
# 解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#
#
# 说明：
#
#
# 矩阵内的矩形区域面积必须大于 0。
# 如果行数远大于列数，你将如何解答呢？
#
#
#


# @lc code=start
class Solution:

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        preSum = [[0 for _ in range(n + 1)] for _ in range(m)]

        # 每一行的前缀和计算
        for i in range(m):
            for j in range(1, n + 1):
                preSum[i][j] = preSum[i][j - 1] + matrix[i][j - 1]

        res = float('-inf')
        for colA in range(1, n + 1):
            for colB in range(colA, n + 1):
                slist, cur = [0], 0
                for row in range(m):
                    # 尝试[colA colB]之间的
                    cur += preSum[row][colB] - preSum[row][colA - 1]
                    # idx = self.bsearch(slist, cur-k)
                    idx = bisect.bisect_left(slist, cur - k)
                    if idx < len(slist): res = max(res, cur - slist[idx])
                    # insert_idx = self.bsearch(slist, cur)
                    # slist.insert(insert_idx, cur)
                    bisect.insort(slist, cur)
        return res


# @lc code=end
