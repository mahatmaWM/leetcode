[树状数组讲解](https://blog.csdn.net/bestsort/article/details/80796531?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

```python
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums[:]
        self.count = [0 for i in xrange(len(nums)+1)]
        for i in xrange(len(nums)):
            self.initialize(i, nums[i])

    def initialize(self, i, val):
        i += 1
        while i < len(self.nums) + 1:
            self.count[i] += val
            # lowbit的操作，保证了logN
            i += (i & -i)

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        self.initialize(i, diff)

    def left_sum(self, i):
        i += 1
        total = 0
        while i>0:
            total += self.count[i]
            i -= (i & -i)
        return total

    def sumRange(self, i, j):
        return self.left_sum(j) - self.left_sum(i-1)
```