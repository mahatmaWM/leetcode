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

# 滑动窗口 思路：
# 1、初始，left指针和right指针都指向S的第一个元素.
# 2、将right指针右移，扩张窗口，直到得到一个可行窗口，亦即包含T的全部字母的窗口。
# 3、得到可行的窗口后，将left指针逐个右移，若得到的窗口依然可行，则更新最小窗口大小。
# 4、若窗口不再可行，则跳转至 2。

# 注意如何检查窗口是否满足条件？？


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
        dict_t = collections.Counter(t)

        # 记录t中去重后字母个数
        required = len(dict_t)
        l, r = 0, 0
        # 用于检查窗口中去重字母是否满足t中需求
        formed = 0
        # 窗口中字母字典
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            # 字母character的个数是否满足t中要求
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            # 窗口中找到的字母都满足要求后，尝试着右移l指针，减少窗口大小
            while l <= r and formed == required:
                character = s[l]
                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                # 右移l指针的时候，要更新窗口字母的计数，同时更新formed变量
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
