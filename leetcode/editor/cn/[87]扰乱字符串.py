# 给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
#
# 下图是字符串 s1 = "great" 的一种可能的表示形式。 
#
#    great
#   /    \
#  gr    eat
# / \    /  \
# g   r  e   at
#           / \
#          a   t
# 
#
# 在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。 
#
# 例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。 
#
#    rgeat
#   /    \
#  rg    eat
# / \    /  \
# r   g  e   at
#           / \
#          a   t
# 
#
# 我们将 "rgeat” 称作 "great" 的一个扰乱字符串。 
#
# 同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。 
#
#    rgtae
#   /    \
#  rg    tae
# / \    /  \
# r   g  ta  e
#       / \
#      t   a
# 
#
# 我们将 "rgtae” 称作 "great" 的一个扰乱字符串。 
#
# 给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。 
#
# 示例 1: 
#
# 输入: s1 = "great", s2 = "rgeat"
# 输出: true
# 
#
# 示例 2: 
#
# 输入: s1 = "abcde", s2 = "caebd"
# 输出: false
# Related Topics 字符串 动态规划


# 递归的思路：
# 终止条件，字符串是否相等，相等则是；判断字符串中字符是否一样，不是则不是
# i 遍历 1至n-1 分割，每次都对比：
# 有两种可能的分割:
# s1左边对应s2左边，右s1边对应s2右边，或者交叉对比
# 这里对应的思想就是，扰动发生在当前节点的左子树，或者 右子树，或者当前节点


# leetcode submit region begin(Prohibit modification and deletion)
import functools


class Solution(object):
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) or \
                    self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[i:]) and \
                    self.isScramble(s1[i:], s2[:i]):
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().isScramble(s1="abcde", s2="caebd"))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
