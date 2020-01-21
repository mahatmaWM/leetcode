# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
#
# 示例 1: 
#
# 
# 输入:
# "tree"
#
# 输出:
# "eert"
#
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
# 
#
# 示例 2: 
#
# 
# 输入:
# "cccaaa"
#
# 输出:
# "cccaaa"
#
# 解释:
# 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
# 注意"cacaca"是不正确的，因为相同的字母必须放在一起。
# 
#
# 示例 3: 
#
# 
# 输入:
# "Aabb"
#
# 输出:
# "bbAa"
#
# 解释:
# 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
# 注意'A'和'a'被认为是两种不同的字符。
# 
# Related Topics 堆 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def frequencySort(self, s: str) -> str:
        import collections
        count = collections.Counter(s)
        count_sort = sorted(count.items(), key=lambda pair: pair[1],
                            reverse=True)
        return ''.join([k * v for (k, v) in count_sort])


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().frequencySort(s="Aabb"))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
