#给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。 
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。 
#
# 示例1: 
#
# 
#输入: s1 = "ab" s2 = "eidbaooo"
#输出: True
#解释: s2 包含 s1 的排列之一 ("ba").
# 
#
# 
#
# 示例2: 
#
# 
#输入: s1= "ab" s2 = "eidboaoo"
#输出: False
# 
#
# 
#
# 注意： 
#
# 
# 输入的字符串只包含小写字母 
# 两个字符串的长度都在 [1, 10,000] 之间 
# 
# Related Topics 双指针 Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        import collections
        cnt1 = collections.Counter(s1)
        cnt2 = collections.Counter(s2)
        if cnt1 == cnt2:
            return True
        else:
            left = 0
            right = len(s1)
            while right < len(s2):
                s2_hash[s2[left]] -= 1
                if s2_hash[s2[left]] == 0:
                    s2_hash.pop(s2[left])
                left += 1
                if s2[right] in s2_hash.keys():
                    s2_hash[s2[right]] += 1
                else:
                    s2_hash[s2[right]] = 1
                right += 1
                if s2_hash == s1_hash:
                    return True
        return False
        
#leetcode submit region end(Prohibit modification and deletion)
