#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (36.25%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 49.6K
# Testcase Example:  '"3+2*2"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
#
# 示例 1:
#
# 输入: "3+2*2"
# 输出: 7
#
#
# 示例 2:
#
# 输入: " 3/2 "
# 输出: 1
#
# 示例 3:
#
# 输入: " 3+5 / 2 "
# 输出: 5
#
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
class Solution:

    def calculate(self, s: str) -> int:

        def compare(op1, op2):
            return op1 in ["*", "/"] and op2 in ["+", "-"]

        def getvalue(num1, num2, operator):
            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            else:  # /
                return num1 // num2

        def process(num_stack, opt_stack):
            operator = opt_stack.pop()
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            num_stack.append(getvalue(num1, num2, operator))

        num_stack = []
        opt_stack = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                pass
            # 数字，入栈num_stack
            elif s[i].isdigit():
                start = i
                while i + 1 < len(s) and s[i + 1].isdigit():
                    i += 1
                num_stack.append(int(s[start:i + 1]))
            # 右括号，opt_stack出栈，同时num_stack出栈并计算，计算结果入栈num_stack，直到opt_stack出栈一个左括号
            elif s[i] == ")":
                while opt_stack[-1] != "(":
                    process(num_stack, opt_stack)
                opt_stack.pop()
            # 操作符栈为空 或者 操作符栈顶为左括号，操作符直接入栈opt_stack
            # 当前操作符为左括号或者比栈顶操作符优先级高，操作符直接入栈opt_stack
            elif not opt_stack or opt_stack[-1] == "(" or s[i] == "(" or compare(s[i], opt_stack[-1]):
                opt_stack.append(s[i])
            else:  # 优先级不比栈顶操作符高时，opt_stack出栈同时num_stack出栈并计算，计算结果如栈num_stack
                while opt_stack and not compare(s[i], opt_stack[-1]):
                    # if opt_stack[-1] == "(":  # 若遇到左括号，停止计算
                    #     break
                    process(num_stack, opt_stack)
                opt_stack.append(s[i])
            i += 1

        while opt_stack:
            process(num_stack, opt_stack)
        return num_stack.pop()


# @lc code=end
