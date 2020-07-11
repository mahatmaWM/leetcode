#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (46.83%)
# Likes:    279
# Dislikes: 0
# Total Accepted:    46K
# Total Submissions: 98.1K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
#
#
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
#
#


# @lc code=start
class Solution:
    # IP的格式每位是在0~255之间,注意不能出现以0开头的两位以上数字,比如012,08..., *.0.* 或者 *.12.* 这种IP才合法
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        n = len(s)

        # start 字符串的开始位置
        # tmp_res 临时结果
        # k IP地址4个部分，还是多少个
        import copy

        def backtrack(start, tmp_res, k):
            if start == n and k == 0:
                # 注意去掉最后的一个.符号
                self.res.append(copy.deepcopy(tmp_res[0:-1]))
                return
            if k < 0: return

            # 尝试[start, start+3)范围内的数字
            for i in range(start, start + 3):
                if i < n:
                    if start == i and s[i] == '0':
                        backtrack(i + 1, tmp_res + s[i] + '.', k - 1)
                        # 注意这里的break是必须的，不能去遍历012这种情况了
                        break
                    if 0 < int(s[start:i + 1]) <= 255: backtrack(i + 1, tmp_res + s[start:i + 1] + '.', k - 1)

        backtrack(0, "", 4)
        return self.res


# @lc code=end
