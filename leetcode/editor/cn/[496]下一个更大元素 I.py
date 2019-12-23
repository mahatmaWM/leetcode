# 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
# 找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
#
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。
# 如果不存在，对应位置输出-1。
#
# 示例 1: 
#
# 
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
#    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
#    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。 
#
# 示例 2: 
#
# 
# 输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
#    对于num1中的数字2，第二个数组中的下一个较大数字是3。
#    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
# 
#
# 注意: 
#
# 
# nums1和nums2中所有元素是唯一的。 
# nums1和nums2 的数组大小都不超过1000。 
# 
# Related Topics 栈

# 解法：递减栈。
#
# 1、求出nums2中所有元素的右边第一个比其大数字，并记录到right_bigger中。
#   具体做法：用递减栈（栈低到栈顶的元素递减），遍历nums2，当当前元素i大于栈顶元素时，就弹出栈顶元素并记录栈顶元素下一个最大值为当前元素i。
#   然后继续比较栈顶元素，直到小于或等于栈顶元素。
#
# 2、循环nums1中的元素，访问在right_bigger中的值。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        right_bigger = {}
        stack = []
        ans = []

        for i in nums2:
            while len(stack) and stack[-1] < i:
                right_bigger[stack.pop()] = i
            stack.append(i)

        for i in nums1:
            ans.append(right_bigger.get(i, -1))

        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = Solution()
    print(a.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
