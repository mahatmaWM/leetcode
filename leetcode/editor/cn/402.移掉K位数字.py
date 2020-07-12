#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#
# https://leetcode-cn.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (29.09%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    18.9K
# Total Submissions: 64.9K
# Testcase Example:  '"1432219"\n3'
#
# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
#
# 注意:
#
#
# num 的长度小于 10002 且 ≥ k。
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
#
#

# @lc code=start
class Solution:
    # 将剩余的数字保留在递增栈中（栈低到栈顶依次减少），那么最终的数字一定是最小的
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return '0'

        incr_stack = []
        for n in num:
            while incr_stack and k and int(incr_stack[-1]) > int(n):
                incr_stack.pop()
                k -= 1
            incr_stack.append(n)
        # 如果还需要从栈中去掉数字
        while k:
            incr_stack.pop()
            k -= 1
        if not incr_stack: return '0'
        return str(int("".join(incr_stack)))

# @lc code=end

