#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (38.05%)
# Likes:    259
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 47.1K
# Testcase Example:  '[5,2,6,1]'
#
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
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
#
#


# @lc code=start
class Solution1:
    # 右侧更小数个数（假如升序排一个数组，那么这就是排序时候逆序对的数目问题），比如冒泡排序时，单这种方法需要n2复杂度。
    # 思路：逆序遍历数组，并维持已遍历数字的有序，然后对于新元素，二分查找到对应的位置索引，就能得到答案
    # 注意bisect模块的使用 bisect_left。
    # 另外，单调栈一般用于找左右比其大或小的第一个元素位置，而本题目是找比其小的元素个数，所以单调栈不适用。
    def countSmaller(self, nums: List[int]) -> List[int]:
        import bisect
        res, visited = [], []
        for num in nums[::-1]:
            res.append(bisect.bisect_left(visited, num))
            bisect.insort(visited, num)
        return res[::-1]


class Solution:
    # 线段树方法
    # 1、首先把数组的 min max 区间创建线段树
    # 2、然后逆序遍历数组，对于数字nums[i]，我们只需要在线段树中寻找[min , nums[i]-1]区间出现的数字个数即可
    # 3、同时遍历的时候把nums[i]更新入线段树
    # 这样的过程就是在模拟整个操作，只是寻找个数这里，利用了线段树logN的特性加速
    def countSmaller(self, nums: List[int]) -> List[int]:

        class SegmentNode:

            def __init__(self, start, end):
                # node节点的区间[start, end]，两边都闭
                self.start = start
                self.end = end
                # 区间元素个数
                self.cnt = 0
                # 左右子树
                self.left = None
                self.right = None

        def buildTree(l, r):
            # if l > r: return None
            if l == r:  # 叶子
                leaf = SegmentNode(l, r)
                return leaf
            root = SegmentNode(l, r)
            mid = (l + r) // 2
            root.left, root.right = buildTree(l, mid), buildTree(mid + 1, r)
            return root

        def updateTree(root, i, val):
            if root.start == root.end:
                root.cnt += val
                return val
            # 递归更新树
            mid = (root.start + root.end) // 2
            if i <= mid:
                updateTree(root.left, i, val)
            else:
                updateTree(root.right, i, val)
            root.cnt = root.left.cnt + root.right.cnt
            return

        def count(root, start, end):
            if start > end: return 0
            # 叶子节点
            if root.start == start and root.end == end: return root.cnt
            mid = (root.start + root.end) // 2
            if end <= mid: return count(root.left, start, end)
            if start > mid: return count(root.right, start, end)
            return count(root.left, start, mid) + count(root.right, mid + 1, end)

        res = list()
        length = len(nums)
        if length == 0: return res
        start, end = min(nums), max(nums)
        # 首先创建一颗从min到max区间的线段树（把节点分配好，不填入值）
        root = buildTree(start, end)
        # 倒序遍历数组，在当前线段树中查找[min,nums[i]-1]之间有多少个数字，这就是nums[i]右边小于它的个数
        for i in range(length - 1, -1, -1):
            res.insert(0, count(root, start, nums[i] - 1))
            # 把nums[i]数字放入线段树，其cnt=1
            updateTree(root, nums[i], 1)
        return res


# @lc code=end
