# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
#
# 说明：
#
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
#
# Related Topics 哈希表 双指针 字符串 Sliding Window

# 思路，滑动窗口
# 1、初始left指针和right指针都指向S的第一个元素。
# 2、将right指针右移，扩张窗口，直到得到一个可行窗口，亦即包含T的全部字母的窗口。（候选解）
# 3、得到可行的窗口后，将left指针逐个右移，若得到的窗口依然可行，则更新最小窗口大小。（优化候选解）
# 4、若窗口不再可行，则跳转至2。
#
# 以上是滑动窗口解这类题的基本套路
# 注意如何检查窗口是否满足条件。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        # 记录t中每个字母出现次数
        import collections
        t_counts = collections.Counter(t)
        uniq_require = len(t_counts)

        left, right = 0, 0
        uniq_formed = 0
        window = {}

        # (window length, left, right)
        ans = float("inf"), None, None

        while right < len(s):
            # 尝试不断右移right指针来找到一个候选集
            character = s[right]
            window[character] = window.get(character, 0) + 1
            # 查看字母character的个数是否满足t中的要求了
            if character in t_counts and \
                    window[character] == t_counts[character]:
                uniq_formed += 1

            # 窗口中找到的字母都满足要求后，尝试着右移left指针，减少窗口大小，更新窗口字母的计数，同时更新formed变量
            while left <= right and uniq_formed == uniq_require:
                character = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window[character] -= 1
                # 查看字母character的个数是否还满足t中的要求
                if character in t_counts and \
                        window[character] < t_counts[character]:
                    uniq_formed -= 1
                left += 1
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().minWindow(s="ab", t="a"))
