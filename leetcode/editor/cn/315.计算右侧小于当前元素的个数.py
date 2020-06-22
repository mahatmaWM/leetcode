# 给定一个整数数组 nums，按要求返回一个新数组 counts。
# 数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于 nums[i] 的元素的数量。
#
# 示例: 
#
# 输入: [5,2,6,1]
# 输出: [2,1,1,0]
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.
# 
# Related Topics 排序 树状数组 线段树 二分查找 分治算法

# 假如升序排一个数组，那么这就是排序时候逆序对的数目问题，比如冒泡排序时，单这种方法需要n2复杂度。
# 本体可以使用Python的bisect模板，在一个有序数组中二分查到找到对应位置，nlogn复杂度。

# 思路：
# 逆序遍历数组，并维持已遍历数字的有序，然后对于新元素，二分查找到对应的位置
# 注意bisect模块的使用 bisect_left。
# 单调栈一般用于找左右比其大或小的第一个元素位置，而本题目是找比其小的元素个数。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        res, visited = [], []
        for num in nums[::-1]:
            res.append(bisect.bisect_left(visited, num))
            bisect.insort(visited, num)
        return res[::-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().countSmaller(nums=[5, 2, 6, 1]))
