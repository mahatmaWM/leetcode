#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (52.22%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    26.9K
# Total Submissions: 51.5K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是质因数只包含 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
# 说明:  
#
#
# 1 是丑数。
# n 不超过1690。
#
#
#

# @lc code=start
class Solution:
    # 1、可以考虑动态规划的思想，第n个丑数是怎么来的？它一定是在第n个丑数之前的n-1个丑数中的任意一个，乘以2、3、5得来的。
    #       现在的问题就是，如何从前n-1个丑数中选出那个丑数来，然后又如何确定是乘以2那，还是3 或者是5那？
    # 2、解决办法，用一个ugly[i]表示第i+1个丑数，维护一系列丑数。
    # 3、用变量i2记录在ugly[]中出现的第一个丑数，且使这个丑数乘以2是否大于ugly[]中最后一个丑数，此时，很显然ugly[i2] * 2就是下一个丑数的备选值，
    #       同理选出ugly[i3] * 3、ugly[i5] * 5，然后从这三个值里面选择最小的作为下一个丑数。
    #    以此类推，直到选出n个来。
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]
# @lc code=end

