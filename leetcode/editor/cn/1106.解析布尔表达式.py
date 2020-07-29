#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达式
#
# https://leetcode-cn.com/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (54.08%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 4.5K
# Testcase Example:  '"!(f)"'
#
# 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。
#
# 有效的表达式需遵循以下约定：
#
#
# "t"，运算结果为 True
# "f"，运算结果为 False
# "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
# "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
# "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
#
#
#
#
# 示例 1：
#
# 输入：expression = "!(f)"
# 输出：true
#
#
# 示例 2：
#
# 输入：expression = "|(f,t)"
# 输出：true
#
#
# 示例 3：
#
# 输入：expression = "&(t,f)"
# 输出：false
#
#
# 示例 4：
#
# 输入：expression = "|(&(t,f,t),!(t))"
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= expression.length <= 20000
# expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
# expression 是以上述形式给出的有效表达式，表示一个布尔值。
#
#
#


# @lc code=start
class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        s = 0

        def parse(exp):
            nonlocal s
            ch = exp[s]
            if ch == 't':
                return True
            if ch == 'f':
                return False
            if ch == '!':
                s += 1
                ans = not parse(exp)
                s += 1
                return ans
            is_and = True if ch == '&' else False
            # is_or = False if ch =='|' else True
            ans = is_and
            s += 1
            while s < len(expression):
                if is_and:
                    ans = ans and parse(exp)
                else:
                    ans = ans or parse(exp)
                ch = exp[s]
                if ch == ')':
                    break
                else:
                    s += 1
            return ans

        return parse(expression)


# @lc code=end
if __name__ == "__main__":
    print(Solution().parseBoolExpr(expression = '!(f)'))
