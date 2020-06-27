#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#
# https://leetcode-cn.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (30.86%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 16.5K
# Testcase Example:  '12'
#
# 给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
#
# 示例 1:
#
#
# 输入: 12
# 输出: 21
#
#
# 示例 2:
#
#
# 输入: 21
# 输出: -1
#
#
#


# @lc code=start
class Solution:

    def nextGreaterElement(self, n: int) -> int:
        n, tail = list(str(n)), []
        for i in range(len(n) - 1, -1, -1):
            # tail保存了倒序遍历n的每位数字的信息，逆序找到一位j比i更大，交换i j的数字，然后把后面的升序排，最后组合成新的数字
            # 方法与31题一样
            for j in tail:
                if n[j] > n[i]:
                    n[j], n[i] = n[i], n[j]
                    m = int(''.join(n[:i + 1] + sorted(n[i + 1:])))
                    return -1 if m > 2**31 - 1 else m
            tail.append(i)
        return -1


if __name__ == "__main__":
    print(Solution().nextGreaterElement(n=21))
# @lc code=end
