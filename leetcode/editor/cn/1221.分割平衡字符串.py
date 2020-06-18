#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#
# https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/description/
#
# algorithms
# Easy (78.34%)
# Likes:    53
# Dislikes: 0
# Total Accepted:    19.4K
# Total Submissions: 24.7K
# Testcase Example:  '"RLRRLLRLRL"'
#
# 在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
#
# 给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
#
# 返回可以通过分割得到的平衡字符串的最大数量。
#
#
#
# 示例 1：
#
# 输入：s = "RLRRLLRLRL"
# 输出：4
# 解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
#
#
# 示例 2：
#
# 输入：s = "RLLLLRRRLR"
# 输出：3
# 解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
#
#
# 示例 3：
#
# 输入：s = "LLLLRRRR"
# 输出：1
# 解释：s 只能保持原样 "LLLLRRRR".
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s[i] = 'L' 或 'R'
# 分割得到的每个字符串都必须是平衡字符串。
#
# 贪心方法，扫描一次字符串即可
#

# @lc code=start
class Solution:

    def balancedStringSplit(self, s: str) -> int:
        count = 0
        count_L = 0
        count_R = 0

        for s_ in s:
            if s_ == 'L':
                count_L += 1
            else:
                count_R += 1

            if count_L == count_R:
                count += 1
        return count


# @lc code=end
