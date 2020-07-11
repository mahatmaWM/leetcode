#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (42.34%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    67K
# Total Submissions: 158.4K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
# 说明：
#
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#
#


# @lc code=start
class Solution:
    # 思路：
    # 1、逆序两个字符串
    # 2、最终结果长度为m+n
    # 3、模拟乘法的计算过程即可
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]

        arr = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i + j] += int(num1[i]) * int(num2[j])
        # print('arr={}'.format(arr))
        ans = []
        for i in range(len(arr)):
            digit = arr[i] % 10
            carry = arr[i] // 10
            if i < len(arr) - 1: arr[i + 1] += carry
            # 逆序了结果
            ans.insert(0, str(digit))
        # print('ans={}'.format(ans))
        while len(ans) > 0 and ans[0] == '0':
            ans.pop(0)
        return '0' if len(ans) == 0 else ''.join(ans)


# @lc code=end
