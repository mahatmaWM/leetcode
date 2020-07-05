#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
# https://leetcode-cn.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (71.95%)
# Likes:    187
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 15.7K
# Testcase Example:  '"2-1-1"'
#
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及
# * 。
#
# 示例 1:
#
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# 示例 2:
#
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#


# @lc code=start
class Solution:
    # 思路：每遇到一个运算符，就分开左右两边，分别递归计算左右
    @functools.lru_cache(maxsize=None)
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input: return []
        if input.isdigit(): return [int(input)]
        res = []
        for k in range(len(input)):
            if input[k] == '+':
                left = self.diffWaysToCompute(input[:k])
                right = self.diffWaysToCompute(input[k + 1:])
                for left_item in left:
                    for right_item in right:
                        res.append(left_item + right_item)
            elif input[k] == '-':
                left = self.diffWaysToCompute(input[:k])
                right = self.diffWaysToCompute(input[k + 1:])
                for left_item in left:
                    for right_item in right:
                        res.append(left_item - right_item)
            elif input[k] == '*':
                left = self.diffWaysToCompute(input[:k])
                right = self.diffWaysToCompute(input[k + 1:])
                for left_item in left:
                    for right_item in right:
                        res.append(left_item * right_item)
        return res


# @lc code=end
