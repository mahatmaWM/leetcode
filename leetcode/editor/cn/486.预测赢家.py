#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#
# https://leetcode-cn.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (51.91%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    7.4K
# Total Submissions: 14.3K
# Testcase Example:  '[1,5,2]'
#
# 给定一个表示分数的非负整数数组。
# 玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，然后玩家1拿，……。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
#
# 给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。
#
# 示例 1:
#
#
# 输入: [1, 5, 2]
# 输出: False
# 解释: 一开始，玩家1可以从1和2中进行选择。
# 如果他选择2（或者1），那么玩家2可以从1（或者2）和5中进行选择。如果玩家2选择了5，那么玩家1则只剩下1（或者2）可选。
# 所以，玩家1的最终分数为 1 + 2 = 3，而玩家2为 5。
# 因此，玩家1永远不会成为赢家，返回 False。
#
#
# 示例 2:
#
#
# 输入: [1, 5, 233, 7]
# 输出: True
# 解释: 玩家1一开始选择1。然后玩家2必须从5和7中进行选择。无论玩家2选择了哪个，玩家1都可以选择233。
# 最终，玩家1（234分）比玩家2（12分）获得更多的分数，所以返回 True，表示玩家1可以成为赢家。
#
#
# 注意:
#
#
# 1 <= 给定的数组长度 <= 20.
# 数组里所有分数都为非负数且不会大于10000000。
# 如果最终两个玩家的分数相等，那么玩家1仍为赢家。
#
# 思路
# https://neetcode-cn.com/probnems/predict-the-winner/sonution/bo-yi-dpmo-ban-san-chong-dpsi-nu-you-hua-kong-jian/
# 最基本的博弈DP模板。
# dp[i][j].fir 表示nums[i]到nums[j]之间 先手拿到的最大分数。
# dp[i][j].sec 表示nums[i]到nums[j]之间 后手拿到的最大分数。
# 这样就能轻松的得到递推公式。
# dp[i][j].fir = max(nums[i]+dp[i+1][j].sec, nums[j]+dp[i][j-1].sec);
# // 先手选左边，获得nums[i]的分数，并得到dp[i+1][j]的后手的分数。
# // 先手选右边，获得nums[j]的分数，并得到dp[i][j-1]的后手的分数。
# dp[i][j].sec = dp[i+1][j].fir or dp[i][j-1].fir;
# // 当前位置后手，即成为对应的先手
#


# @lc code=start
class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[[0, 0]] * n for _ in range(n)]

        for i in range(n):
            dp[i][i][0] = nums[i]
            dp[i][i][1] = 0

        # 斜着遍历数组
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # 先手选择最左边或者最右边的分数
                left = nums[i] + dp[i + 1][j][1]
                right = nums[j] + dp[i][j - 1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]

        return dp[0][n - 1][0] >= dp[0][n - 1][1]


# @lc code=end
