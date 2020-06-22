# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 
#
# 示例: 
#
# 
# s = "3[a]2[bc]", 返回 "aaabcbc".
# s = "3[a2[c]]", 返回 "accaccacc".
# s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
# 
# Related Topics 栈 深度优先搜索

# 注意的地方是数字可能是111这样的大于10的数字
# 字母要考虑大小写
# 左右括号要对应
# num_stack保存数字，other_stack保存字母串和[]。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        other_stack = []

        i = 0
        res = ''
        while i < len(s):
            if '1' <= s[i] <= '9':
                index = i
                while i + 1 < len(s) and '0' <= s[i + 1] <= '9':
                    i += 1
                num_stack.append(int(s[index:i + 1]))
            elif s[i] == '[':
                other_stack.append('[')
            elif ('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z'):
                temp_str = s[i]
                while i + 1 < len(s) and (('a' <= s[i + 1] <= 'z') or ('A' <= s[i + 1] <= 'Z')):
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

# leetcode submit region end(Prohibit modification and deletion)
