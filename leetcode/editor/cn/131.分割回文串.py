#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (67.89%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    34.3K
# Total Submissions: 50.4K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0: return []
        res = []

        # 回溯的路径为start，选择列表为tmp_list
        def backtrack(start, tmp_list):
            nonlocal res
            if start == len(s):
                res.append(copy.deepcopy(tmp_list))
                return
            for end in range(start + 1, len(s) + 1):
                cur_str = s[start:end]
                # 如果当前子串为回文串，则可以继续递归并回溯，不是回文的被剪掉
                if cur_str == cur_str[::-1]:
                    tmp_list.append(cur_str)
                    backtrack(end, tmp_list)
                    tmp_list.pop()

        backtrack(0, [])
        return res
# @lc code=end

