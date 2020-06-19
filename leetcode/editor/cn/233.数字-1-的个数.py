#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# https://leetcode-cn.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (36.15%)
# Likes:    135
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 22.6K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
# 示例:
#
# 输入: 13
# 输出: 6
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
#
# 题解的这个思路没有看懂？？？

# @lc code=start
class Solution:

    def countDigitOne(self, n: int) -> int:
        self.num = 1
        a = [0] * 11

        dp = [[[-1] * 11 for i in range(11)] for j in range(11)]

        def dfs(pos, now, tot, lead, limit):
            if pos == 0:
                return now == tot
            if not limit and not lead and dp[pos][now][tot] != -1:
                return dp[pos][now][tot]
            up = a[pos] if limit else 9
            res = 0
            for i in range(0, up + 1):
                if lead and i == 0:
                    res += dfs(pos - 1, now, tot, True, limit and i == a[pos])
                else:
                    res += dfs(pos - 1, now + (i == self.num), tot, lead and i == 0, limit and i == a[pos])
            if not limit and not lead:
                dp[pos][now][tot] = res
            return res

        def solve(x):
            lennum = 1
            while x:
                a[lennum] = x % 10
                x = x // 10
                lennum += 1
            lennum -= 1
            ans = [0] * 11
            total = 0
            for j in range(1, lennum + 1):
                ans[j] = dfs(lennum, 0, j, True, True)
                total += j * ans[j]
            return total

        return solve(n) if n > 0 else 0


def main():
    print('res={}'.format(Solution().countDigitOne(13)))


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    main()
    print("%s sec" % (time.perf_counter() - start))

# @lc code=end
