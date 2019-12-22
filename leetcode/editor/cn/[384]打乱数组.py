# 打乱一个没有重复元素的数组。
#
# 示例: 
#
# 
# // 以数字集合 1, 2 和 3 初始化数组。
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
# solution.shuffle();
#
# // 重设数组到它的初始状态[1,2,3]。
# solution.reset();
#
# // 随机返回数组[1,2,3]打乱后的结果。
# solution.shuffle();
# 
#

# 思路：
# 涉及到随机打乱，类似洗牌算法，通过生成随机数字的索引，来交换数组中的元素，达到打乱的目的。
# 这里重置需要注意python的特性，[:]或者deepcopy避免引用带来的问题。

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], \
                                                  self.array[i]
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# leetcode submit region end(Prohibit modification and deletion)
def main():
    nums = [1, 2, 3, 5, 6, 7]
    obj = Solution(nums)
    print(obj.reset())
    print(obj.shuffle())
    print(obj.reset())


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
