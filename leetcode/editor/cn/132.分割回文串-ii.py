#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (43.05%)
# Likes:    151
# Dislikes: 0
# Total Accepted:    11.7K
# Total Submissions: 27.2K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回符合要求的最少分割次数。
#
# 示例:
#
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#
#
#


# @lc code=start
class Solution1:
    # 思路：递归做法，复杂度是O(n!)
    @functools.lru_cache(None)
    def minCut(self, s: str) -> int:
        if s == s[::-1]: return 0
        ans = float("inf")
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                ans = min(self.minCut(s[i:]) + 1, ans)
        return ans


class Solution:
    # 初始化最小分割次数数组min_cut=[0,1,2,……,n-1]，长度为字符串的长度n。
    # 其中min_cut[i]表示s[0,1,2,…… i]的每个子串都是回文串的分割次数。
    # 初始化的含义为，s[0]只有一个字符不需要分割，因此min_cut[0]=0，
    # s[0,1]最多需要1次，分成两个单独的字符。s[0,1,2]需要三次。以此类推。
    #
    # 初试化dp[start][end]表示s[start,⋯,end]是否为回文串。
    # 遍历dp，子串结束索引为end，遍历区间[0,n)：
    #   子串开始索引start，遍历区间[0,end+1)：
    #       如果s[start]==s[end] 并且 end−start<2 or dp[start+1][end−1]==True。
    #       【 上句解释：若s[start]==s[end]表示子串s[start,⋯,end]的两端相同，则该子串是否为回文串取决于dp[start+1][end−1] 即s[start+1,⋯,end−1]是否为回文串。
    #          特殊情况是end−start<2，表示长度小于3，此时也是满足的。
    #        】
    #           dp[start][end]s[start,⋯,end]为回文子串）为True
    #           若start==0，开始位置为0，说明s[0,⋯,j]为回文串，则此时min_cut[end]=0，表示到end位置的子串不需要进行切割，自身就是回文子串。
    #           若start!=0，说明开始的位置不是0，此时min_cut[end]=min(min_cut[end],min_cut[start−1]+1)，表示始终为到上一回文串位置的切割次数加1中的最小值。
    # 返回min_cut[−1]
    def minCut(self, s: str) -> int:
        n = len(s)
        min_cut = list(range(n))
        dp = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end + 1):
                # 如果s[start, end]为回文，
                # 如果start=0，说明这一段可以一次切分，则min_cut[end]为0
                # 如果start!=0，则此时的min_cut[end]应该为start前一位的切分数字+1有关，更新最小值
                if s[start] == s[end] and (end - start < 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    if start == 0:
                        min_cut[end] = 0
                    else:
                        min_cut[end] = min(min_cut[end], min_cut[start - 1] + 1)
        return min_cut[-1]


# @lc code=end
