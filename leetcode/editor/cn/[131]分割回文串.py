# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。 
#
# 示例: 
#
# 输入: "aab"
# 输出:
# [
#  ["aa","b"],
#  ["a","a","b"]
# ]
# Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def __init__(self):
        self.res = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0: return []

        # 回溯的路径为start，选择列表为tmp_list
        def backtrack(start, tmp_list):
            if start == len(s):
                self.res.append(tmp_list[:])
                return
            for end in range(start + 1, len(s) + 1):
                cur_str = s[start:end]
                # 如果当前子串为回文串，则可以继续递归并回溯
                # 不是回文的被剪掉
                if cur_str == cur_str[::-1]:
                    tmp_list.append(cur_str)
                    backtrack(end, tmp_list)
                    tmp_list.pop()

        backtrack(0, [])
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().partition(s="aab"))
