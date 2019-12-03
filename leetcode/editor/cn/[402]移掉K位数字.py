# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
#
# 注意: 
#
# 
# num 的长度小于 10002 且 ≥ k。 
# num 不会包含任何前导零。 
# 
#
# 示例 1 : 
#
# 
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
# 
#
# 示例 2 : 
#
# 
# 输入: num = "10200", k = 1
# 输出: "200"
# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# 
#
# 示例 3 : 
#
# 
# 输入: num = "10", k = 2
# 输出: "0"
# 解释: 从原数字移除所有的数字，剩余为空就是0。
# 
# Related Topics 栈 贪心算法


# 看了Topics知道这个是用栈来解决的题目，看了别人的解答才明白怎么回事。
#
# 使用一个栈作为辅助，遍历数字字符串，当当前的字符比栈最后的字符小的时候，说明要把栈的最后的这个字符删除掉。
# 为什么呢？你想，把栈最后的字符删除掉，然后用现在的字符进行替换，是不是数字比以前的那种情况更小了？所以同样的道理，做一个while循环！这个很重要，可是我没有想到。
# 在每一个数字处理的时候，都要做一个循环，使得栈里面最后的数字比当前数字大的都弹出去。
#
# 最后，如果K还没用完，那要删除哪里的字符呢？毋庸置疑肯定是最后的字符，因为前面的字符都是小字符。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return '0'
        stack = []
        for n in num:
            while stack and k and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)

        while k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        return str(int("".join(stack)))

# leetcode submit region end(Prohibit modification and deletion)
