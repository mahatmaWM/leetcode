# 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。 
#
# 示例 1: 
#
# 
# 输入: [4,2,3]
# 输出: True
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
# 
#
# 示例 2: 
#
# 
# 输入: [4,2,1]
# 输出: False
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 
#
# 说明: n 的范围为 [1, 10,000]。 
# Related Topics 数组

# 思路，复制2个数组(a,b)出来，只要碰到 nums[i]>nums[i+1] 的情况，
# 前一个数组（a）直接删除 nums[i] 再比较删除后的数组是否是已经排序好的（a 是不是等于 sorted(a) )，
# 后一个数组（b）直接删除 nums[i+1] 再比较删除后的数组是否是已经排序好的（b 是不是等于 sorted(b) )，
# 只要二者之间有一个是已经排序好的就返回 True 否则 返回 False。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True

        import copy
        a, b = copy.deepcopy(nums[:]), copy.deepcopy(nums[:])
        for i in range(len(nums) - 1):
            if a[i] > a[i + 1]:
                del a[i]
                del b[i + 1]
        return (a == sorted(a)) or (b == sorted(b))


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().checkPossibility(nums=[1,2,3]))
