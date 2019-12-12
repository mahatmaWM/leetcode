# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例: 
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
# Related Topics 字符串 回溯算法

# IP的格式每位是在0~255之间,注意不能出现以0开头的两位以上数字,比如012,08...
# *.0.* 或者 *.12.* 这种IP才合法

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(s)

        # flag是需要找多少IP数字
        # tmp是临时结果
        # i是遍历到字符串s的位置
        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return

            # 当起始位置为i是，可以尝试[i, i+3)范围内的数字
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        # 注意这里的break是必须的，不能去遍历012这种情况了
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res

# leetcode submit region end(Prohibit modification and deletion)
