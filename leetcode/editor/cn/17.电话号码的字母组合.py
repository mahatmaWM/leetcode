#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (53.68%)
# Likes:    753
# Dislikes: 0
# Total Accepted:    121.1K
# Total Submissions: 225.7K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
#


# @lc code=start
class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        self.output = []
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(tmp_res, next_digits):
            if len(next_digits) == 0:
                self.output.append(tmp_res)
            else:
                for letter in phone[next_digits[0]]:
                    # 选择
                    tmp_res = tmp_res + letter
                    backtrack(tmp_res, next_digits[1:])
                    # 取消选择
                    tmp_res = tmp_res[:-1]

        backtrack("", digits)
        return self.output


# @lc code=end
