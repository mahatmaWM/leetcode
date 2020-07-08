#
# @lc app=leetcode.cn id=1138 lang=python3
#
# [1138] 字母板上的路径
#
# https://leetcode-cn.com/problems/alphabet-board-path/description/
#
# algorithms
# Medium (40.44%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 8.7K
# Testcase Example:  '"leet"'
#
# 我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。
#
# 在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。
#
#
#
# 我们可以按下面的指令规则行动：
#
#
# 如果方格存在，'U' 意味着将我们的位置上移一行；
# 如果方格存在，'D' 意味着将我们的位置下移一行；
# 如果方格存在，'L' 意味着将我们的位置左移一列；
# 如果方格存在，'R' 意味着将我们的位置右移一列；
# '!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
#
#
# （注意，字母板上只存在有字母的位置。）
#
# 返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。
#
#
#
# 示例 1：
#
# 输入：target = "leet"
# 输出："DDR!UURRR!!DDD!"
#
#
# 示例 2：
#
# 输入：target = "code"
# 输出："RR!DDRR!UUL!R!"
#
#
#
#
# 提示：
#
#
# 1 <= target.length <= 100
# target 仅含有小写英文字母。
#
#
#


# @lc code=start
class Solution:
    # 把每个字母转化为字母板上的坐标，然后通过求两个坐标之间的曼哈顿路径（只能 横着 或者 竖着 移动）即可
    # 正常情况 先移动行再移动列。但是Z比较特殊，只有1列，如果当前字符是z，需要首先移动列
    # 对于移动方向的计算，需要以前一个字符的坐标和当前字符的坐标作对比
    def alphabetBoardPath(self, target: str) -> str:
        d = {}
        for i in range(97, 123):
            d[chr(i)] = ((i - 97) // 5, (i - 97) % 5)

        start = (0, 0)
        ans = ''
        for i in range(len(target)):
            cur = d[target[i]]
            # 如果当前字母是z
            if cur == (5, 0):
                if cur[1] >= start[1]:
                    ans += (cur[1] - start[1]) * 'R'
                else:
                    ans += (start[1] - cur[1]) * 'L'

                if cur[0] >= start[0]:
                    ans += (cur[0] - start[0]) * 'D'
                else:
                    ans += (start[0] - cur[0]) * 'U'
            else:
                if cur[0] >= start[0]:
                    ans += (cur[0] - start[0]) * 'D'
                else:
                    ans += (start[0] - cur[0]) * 'U'

                if cur[1] >= start[1]:
                    ans += (cur[1] - start[1]) * 'R'
                else:
                    ans += (start[1] - cur[1]) * 'L'
            ans += '!'
            start = cur
        return ans


# @lc code=end
