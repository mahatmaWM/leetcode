#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#
# https://leetcode-cn.com/problems/reorganize-string/description/
#
# algorithms
# Medium (41.27%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 20.2K
# Testcase Example:  '"aab"'
#
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
#
# 若可行，输出任意可行的结果。若不可行，返回空字符串。
#
# 示例 1:
#
#
# 输入: S = "aab"
# 输出: "aba"
#
#
# 示例 2:
#
#
# 输入: S = "aaab"
# 输出: ""
#
#
# 注意:
#
#
# S 只包含小写字母并且长度在[1, 500]区间内。
#
#
#


# @lc code=start
class Solution:
    # 贪心算法
    # 1、将字母按照出现次数从大到小排序。
    # 2、每次优先选择剩余次数最多，且与新字符串末尾字符串不重复的字符，排在末尾。
    # 3、若某次选择无法找出这样的字符，则返回空串。
    def reorganizeString(self, S: str) -> str:
        cnt = collections.Counter(S)

        ans = ''
        while cnt:
            stop = True
            for v, c in cnt.most_common():
                if ans == '' or v != ans[-1]:
                    stop = False
                    ans += v
                    cnt[v] -= 1
                    # 删除剩余个数为0的字母
                    if not cnt[v]: del cnt[v]
                    break
            if stop: break
        return ans if len(ans) == len(S) else ''


# @lc code=end
