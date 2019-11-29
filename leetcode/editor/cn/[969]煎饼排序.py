# 给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。
#
# 返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。 
#
# 
#
# 示例 1： 
#
# 输入：[3,2,4,1]
# 输出：[4,2,4,3]
# 解释：
# 我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
# 初始状态 A = [3, 2, 4, 1]
# 第一次翻转后 (k=4): A = [1, 4, 2, 3]
# 第二次翻转后 (k=2): A = [4, 1, 2, 3]
# 第三次翻转后 (k=4): A = [3, 2, 1, 4]
# 第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。
# 
#
# 示例 2： 
#
# 输入：[1,2,3]
# 输出：[]
# 解释：
# 输入已经排序，因此不需要翻转任何内容。
# 请注意，其他可能的答案，如[3，3]，也将被接受。
# 
#
# 
#
# 提示： 
#
# 
# 1 <= A.length <= 100 
# A[i] 是 [1, 2, ..., A.length] 的排列 
# 
# Related Topics 排序 数组

# 第一步，每次找到还没排序的数字之中最大的数字的位置，把这个位置之前的数字翻转，这一步使得最大数字去了最前面。
# 第二步，再次翻转，把最大位置翻到准确的位置上去。
# 这个题目一个比较好的地方是，给的数字是1~N的全排列，所以我们每次要找哪个数字很容易确定，不需要O(N)的遍历去判断最大的数字是谁。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        res = []
        for x in range(N, 0, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res

# leetcode submit region end(Prohibit modification and deletion)
