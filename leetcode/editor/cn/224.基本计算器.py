#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (38.02%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    14.8K
# Total Submissions: 39K
# Testcase Example:  '"1 + 1"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
# 字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
#
# 示例 1:
#
# 输入: "1 + 1"
# 输出: 2
#
#
# 示例 2:
#
# 输入: " 2-1 + 2 "
# 输出: 3
#
# 示例 3:
#
# 输入: "(1+(4+5+2)-3)+(6+8)"
# 输出: 23
#
# 说明：
#
#
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。
#
#
#


# @lc code=start
class Solution1:
    def __init__(self) -> None:
        self.index = 0
    # 与227题不一样
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        return self.get(s)

    # 因为有括号嵌套，所以采用递归的思路，遇到括号就递归调用get函数
    # 而get函数负责处理没有括号的表达式
    # res是当前已经算好的结果，cur是目前的数字，pre_op是cur数字之前的符号+-
    def get(self, s):
        if self.index >= len(s): return 0
        res = 0
        pre_op = '+'
        while self.index < len(s):
            cur = 0
            if s[self.index] == '(':
                self.index += 1
                cur = self.get(s)
            else:
                while self.index < len(s) and s[self.index].isdigit():
                    cur = cur * 10 + int(s[self.index])
                    self.index += 1

            if pre_op == '+':
                res += cur
            elif pre_op == '-':
                res -= cur

            if self.index < len(s) and s[self.index] == ')':
                self.index += 1
                return res
            # 更新pre_op
            if self.index < len(s) and s[self.index] in ['+', '-']:
                pre_op = s[self.index]

            self.index += 1
        return res


class Solution:
    # 用栈来实现，和上面的递归一样的思路
    # 遇到（ 时，把先前已经计算好的res 和 pre_op 存放到stack里面，然后开始计算当前括号里面的内容
    # 遇到 ）时，说明括号里面的内容计算完毕，然后把之前stack里面保存的结果弹出更新结果
    # 最后当所有数字结束的时候，需要把结果进行计算，确保结果是正确的。
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        res, cur_num, pre_op = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                cur_num = 10 * cur_num + int(c)
            elif c == "+" or c == "-":
                res = res + pre_op * cur_num
                cur_num = 0
                pre_op = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(pre_op)
                res = 0
                pre_op = 1
            elif c == ")":
                res = res + pre_op * cur_num
                cur_num = 0
                res = res * stack.pop()
                res = stack.pop() + res
        res = res + pre_op * cur_num
        return res


# @lc code=end

if __name__ == "__main__":
    print(Solution().calculate(s="(6)-(8)-(7)+(1+(6))"))
