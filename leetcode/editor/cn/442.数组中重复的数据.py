# 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
#
# 找到所有出现两次的元素。 
#
# 你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？ 
#
# 示例： 
#
# 
# 输入:
# [4,3,2,7,8,2,3,1]
#
# 输出:
# [2,3]
# 
# Related Topics 数组

# 思路：
# 两点需要注意，1、数字范围1 到 n；2、不能用额外空间。
# 这种不能用额外空间意味着只能在原始数组上操作，而且数字范围又合适，所以用数字代表下标来更新对应位置的数字，
# 比如第一次变为负数，第二次再遇到负数，就说明此下标对应的数字出现了两次。

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num - 1] < 0:
                res.append(abs_num)
            else:
                nums[abs_num - 1] = -nums[abs_num - 1]
        return res


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
