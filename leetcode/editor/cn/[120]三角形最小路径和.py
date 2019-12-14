# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形： 
#
# [
#     [2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]
# ]
# 
#
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。 
#
# 说明： 
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。 
# Related Topics 数组 动态规划

# 思路，采用从最后一行往上走的方式。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 常规的动态规划dp[i][j]，从最后一层往上走
        # 状态转移只能 dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        # 空间复杂度为On2
        n = len(triangle)
        dp = [[float('inf')] * n for _ in range(n)]
        dp[-1] = triangle[-1]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]

    def minimumTotal(self, triangle):
        # 以上同样的思路，可以原位更改元素，不使用额外空间
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] = min(triangle[i + 1][j],
                                     triangle[i + 1][j + 1]) + triangle[i][j]
        return triangle[0][0]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(Solution().minimumTotal(triangle=triangle))
