#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
# https://leetcode-cn.com/problems/decode-string/description/
#
# algorithms
# Medium (52.74%)
# Likes:    405
# Dislikes: 0
# Total Accepted:    50.4K
# Total Submissions: 95.7K
# Testcase Example:  '"3[a]2[bc]"'
#
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#
#
# 示例 1：
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#
#
# 示例 2：
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
#
#
# 示例 3：
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#
#
# 示例 4：
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#
#
#

# @lc code=start
class Solution:
    # 注意的地方是数字可能是111这样的大于10的数字
    # 字母要考虑大小写
    # 左右括号要对应
    # num_stack保存数字，other_stack保存字母串和[]符号
    def decodeString(self, s: str) -> str:
        num_stack = []
        other_stack = []

        i = 0
        res = ''
        while i < len(s):
            # 数字入栈
            if '1' <= s[i] <= '9':
                index = i
                while i + 1 < len(s) and '0' <= s[i + 1] <= '9':
                    i += 1
                num_stack.append(int(s[index:i + 1]))
            elif s[i] == '[':
                other_stack.append('[')
            # 字符串入栈
            elif 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
                temp_str = s[i]
                while i + 1 < len(s) and ('a' <= s[i + 1] <= 'z' or 'A' <= s[i + 1] <= 'Z'):
                    temp_str += s[i + 1]
                    i += 1
                other_stack.append(temp_str)
            elif s[i] == ']':
                b1 = num_stack.pop()
                temp = ''
                while other_stack[-1] != '[':
                    temp = other_stack.pop() + temp
                tstr = b1 * temp
                # pop [
                other_stack.pop()

                while len(other_stack) > 0 and other_stack[-1] != '[':
                    tstr = other_stack.pop() + tstr
                other_stack.append(tstr)
            i += 1
        while len(other_stack) > 0:
            res = other_stack.pop() + res
        return res
# @lc code=end

