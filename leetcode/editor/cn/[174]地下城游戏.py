# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。
# 我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
#
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。 
#
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
# 其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
#
# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。 
#
# 
#
# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。 
#
# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
# -2(K)  -3  3
# -5    -10  1
# 10    30  -5(P)
# 说明:
# 骑士的健康点数没有上限。 
# 
# 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。 
# Related Topics 二分查找 动态规划

# 思路：
# 设置一个同样大小的dp数组，记录骑士在dp[i][j]位置所需要的最少生命数字，开始条件为dp[-1][-1]为6（6-5=1）。
# 这样可以动态规划，最后计算dp[0][0]位置需要的最小生命数字。
# 注意 因为骑士只能向右向下行走，则dp迭代只能向左向上。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])

        # 最后一行、最后一列的迭代
        for i in range(n - 2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i + 1] - dungeon[-1][i])
        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j],
                               1)
        return dp[0][0]

# leetcode submit region end(Prohibit modification and deletion)
