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
        self.res = []
        n = len(s)

        def backtrack(start, tmp_res, k):
            if start == n and k == 0:
                self.res.append(tmp_res[:-1])
                return
            if k < 0:
                return

            # 当起始位置为i时，可以尝试[i, i+3)范围内的数字
            for j in range(start, start + 3):
                if j < n:
                    if start == j and s[j] == "0":
                        backtrack(j + 1, tmp_res + s[j] + ".", k - 1)
                        # 注意这里的break是必须的，不能去遍历012这种情况了
                        break
                    if 0 < int(s[start:j + 1]) <= 255:
                        backtrack(j + 1, tmp_res + s[start:j + 1] + ".", k - 1)

        backtrack(0, "", 4)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().restoreIpAddresses(s="25525511135"))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
