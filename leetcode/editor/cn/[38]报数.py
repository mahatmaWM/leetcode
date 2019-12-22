# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
#
# 1 被读作 "one 1" ("一个一") , 即 11。 
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2", "one 1" （"一个二" , "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。 
#
# 注意：整数顺序将表示为一个字符串。 
#
# 
#
# 示例 1: 
#
# 输入: 1
# 输出: "1"
# 
#
# 示例 2: 
#
# 输入: 4
# 输出: "1211"
# 
# Related Topics 字符串

# 思路：
# count函数中使用二维数组来记录数字出现的个数

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def count(snum):
            num_count = []
            before = ""
            for s in snum:
                if s != before:
                    num_count.append(["1" + s])
                    before = s
                else:
                    # print(num_count[-1][0][0])
                    num_count[-1] = [str(int(num_count[-1][0][0]) + 1) + s]
            res = ""
            for n in num_count:
                res = res + n[0]
            return res

        i = 1
        snum = "1"
        while i < n:
            snum = count(snum)
            i += 1
        return snum


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().countAndSay(n=4))
