#实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。 
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
#
# 必须原地修改，只允许使用额外常数空间。 
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。 
#1,2,3 → 1,3,2 
#3,2,1 → 1,2,3 
#1,1,5 → 1,5,1 
# Related Topics 数组

# 很有技巧的题目。
# 先找到从后向前数，第一个降序的位置，把此位置后面的翻转。再把这个降序数字和后面第一个比它大的位置交换即可。
# 首先说一下这题怎么想到的。有如下的一个数组
# 1　　2　　7　　4　　3　　1
# 下一个排列为：
# 1　　3　　1　　2　　4　　7
#
# 观察可以发现，再给出的数组中，2之后的数字都是降序排列的，我们把2后面第一个比2大的数字放到最前面，然后让3后面的数字升序排列。
# 简单思路的证明：从7开始是降序的，也就是说7 4 3 1不可能通过重新排列构成更大的数字。如果要得到next permutation，那么必须把2这个位置的数字给换掉才行，而且只能换成比2大的数字在才能使next permutation > current permutation.至于换成多大的数字，很明显的需要换成在2后面的数字中刚好比2大的数字，证明可以使用反证法来说明换成其他数字要么比当前数字小，要么大于正确的next permutation.


#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.reverse(nums, i, n - 1)
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    self.swap(nums, i - 1, j)
                    break

    def reverse(self, nums, i, j):
        """
        contains i and j.
        """
        for k in range(i, (i + j) / 2 + 1):
            self.swap(nums, k, i + j - k)

    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]
        
#leetcode submit region end(Prohibit modification and deletion)
