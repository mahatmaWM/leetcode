# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#
# 示例 1: 
#
# 输入: [10,2]
# 输出: 210
#
# 示例 2: 
#
# 输入: [3,30,34,5,9]
# 输出: 9534330
#
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。 
# Related Topics 排序

# 注意排序的规则

# leetcode submit region begin(Prohibit modification and deletion)
class compare(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest = sorted([str(v) for v in nums], key=compare)
        largest = ''.join(largest)

        return '0' if largest[0] == '0' else largest


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().largestNumber(nums=[3, 30, 34, 5, 9]))
