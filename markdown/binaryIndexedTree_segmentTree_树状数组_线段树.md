
# 两者的区别和联系

两者的区别和联系如下：
1.两者在复杂度上同级, 但是树状数组的常数明显优于线段树, 其编程复杂度也远小于线段树.
2.树状数组的作用被线段树完全涵盖, 凡是可以使用树状数组解决的问题, 使用线段树一定可以解决, 但是线段树能够解决的问题树状数组未必能够解决.
3.树状数组的突出特点是其编程的极端简洁性, 使用lowbit技术可以在很短的几步操作中完成树状数组的核心操作，其代码效率远高于线段树。

# 树状数组
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


# 线段树

## 线段树定义
线段树（segment tree），用来存放给定区间（segment, or interval）内对应信息的一种数据结构。
树状数组（binary indexed tree）相似，线段树也用来处理数组相应的区间查询（range query）和元素更新（update）操作。
与树状数组不同的是，线段树不止可以适用于**区间求和**的查询，也可以进行**区间最大值，区间最小值，区间异或值**的查询，具体的用途涉及到线段树节点的设计，下文代码例子以307题区间求和举例。
和树状数组一样，线段树进行更新（update）的操作为O(logn)，进行区间查询（range query）的操作也为O(logn)

## 线段树实现原理
从数据结构的角度来说，线段树是用一个完全二叉树来存储对应于其每一个区间（segment）的数据。该二叉树的每一个结点中保存着相对应于这一个区间的信息。同时，线段树所使用的这个二叉树是用一个数组保存的，与堆（Heap）的实现方式相同。

例如，给定一个长度为N的数组arr，其所对应的线段树T各个结点的含义如下：
1. T的根结点代表整个数组所在的区间对应的信息，及arr[0:N]（不含N）所对应的信息。
2. T的每一个叶结点存储对应于输入数组的每一个单个元素构成的区间arr[i]所对应的信息，此处0≤i<N。
3. T的每一个中间结点存储对应于输入数组某一区间arr[i:j]对应的信息，此处0≤i<j<N。

以根结点为例，根结点代表arr[0:N]区间所对应的信息，接着根结点被分为两个子树，分别存储arr[0:(N-1)/2]及arr[(N-1)/2+1:N]两个子区间对应的信息。也就是说，对于每一个结点，其左右子结点分别存储母结点区间拆分为两半之后各自区间的信息。也就是说对于长度为N的输入数组，线段树的高度为logN。对于一个线段树来说，其应该支持的两种操作为：
1. Update：更新输入数组中的某一个元素并对线段树做相应的改变。
2. Query：用来查询某一区间对应的信息（如最大值，最小值，区间和等）。


## 线段树的初始化
一般可以借鉴二叉树构建的方式，递归构建线段树。见307题的例子：
``` python
# 左右区间
def buildTree(l, r):
    if l > r: return None
    if l == r:  # 叶子
        n = SegmentNode(l, r)
        n.sum = nums[l]
        return n
    root = SegmentNode(l, r)
    mid = (l + r) // 2
    root.left, root.right = buildTree(l, mid), buildTree(mid + 1, r)
    root.sum = root.left.sum + root.right.sum
    return root
```

## 节点更新
更新一个线段树的过程与上述构造线段树的过程相同。当输入数组中位于i位置的元素被更新时，我们只需从这一元素对应的叶子结点开始，沿二叉树的路径向上更新至更结点即可。显然，这一过程是一个O(logn)的操作。
```python
def updateTree(root, i, val):
    if root.start == root.end:
        root.sum = val
        return val
    # 递归更新树
    mid = (root.start + root.end) // 2
    if i <= mid:
        updateTree(root.left, i, val)
    else:
        updateTree(root.right, i, val)
    root.sum = root.left.sum + root.right.sum
    return root.sum
```

## 区间查询
区间查询大体上可以分为3种情况讨论：
1. 当前结点所代表的区间完全位于给定需要被查询的区间之外，则不应考虑当前结点
2. 当前结点所代表的区间完全位于给定需要被查询的区间之内，则可以直接查看当前结点的母结点
3. 当前结点所代表的区间部分位于需要被查询的区间之内，部分位于其外，则我们先考虑位于区间外的部分，后考虑区间内的（注意总有可能找到完全位于区间内的结点，因为叶子结点的区间长度为1，因此我们总能组合出合适的区间）
```python
def findNode(root, x, y):
    # 叶子节点
    if root.start == x and root.end == y: return root.sum
    mid = (root.start + root.end) // 2
    if y <= mid: return findNode(root.left, x, y)
    if x > mid: return findNode(root.right, x, y)
    return findNode(root.left, x, mid) + findNode(root.right, mid + 1, y)
```