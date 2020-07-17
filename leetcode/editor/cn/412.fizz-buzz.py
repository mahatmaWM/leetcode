#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode-cn.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (63.79%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    39K
# Total Submissions: 60.8K
# Testcase Example:  '1'
#
# 写一个程序，输出从 1 到 n 数字的字符串表示。
#
# 1. 如果 n 是3的倍数，输出“Fizz”；
#
# 2. 如果 n 是5的倍数，输出“Buzz”；
#
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
#
# 示例：
#
# n = 15,
#
# 返回:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
#
#
#


# @lc code=start
class Solution:

    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans


# @lc code=end
