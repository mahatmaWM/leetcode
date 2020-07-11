<!-- TOC -->

- [特殊数字的16进制与二级制对应关系](#%E7%89%B9%E6%AE%8A%E6%95%B0%E5%AD%97%E7%9A%8416%E8%BF%9B%E5%88%B6%E4%B8%8E%E4%BA%8C%E7%BA%A7%E5%88%B6%E5%AF%B9%E5%BA%94%E5%85%B3%E7%B3%BB)
- [二进制运算](#%E4%BA%8C%E8%BF%9B%E5%88%B6%E8%BF%90%E7%AE%97)
    - [特殊的取余操作](#%E7%89%B9%E6%AE%8A%E7%9A%84%E5%8F%96%E4%BD%99%E6%93%8D%E4%BD%9C)
    - [给定数字的二进制表示中1出现的个数](#%E7%BB%99%E5%AE%9A%E6%95%B0%E5%AD%97%E7%9A%84%E4%BA%8C%E8%BF%9B%E5%88%B6%E8%A1%A8%E7%A4%BA%E4%B8%AD1%E5%87%BA%E7%8E%B0%E7%9A%84%E4%B8%AA%E6%95%B0)
    - [将数字n的第bit位 置1](#%E5%B0%86%E6%95%B0%E5%AD%97n%E7%9A%84%E7%AC%ACbit%E4%BD%8D-%E7%BD%AE1)
    - [将数字n的第bit位 置0](#%E5%B0%86%E6%95%B0%E5%AD%97n%E7%9A%84%E7%AC%ACbit%E4%BD%8D-%E7%BD%AE0)
    - [数字n的第bit位 是否为0](#%E6%95%B0%E5%AD%97n%E7%9A%84%E7%AC%ACbit%E4%BD%8D-%E6%98%AF%E5%90%A6%E4%B8%BA0)
    - [删除从右边起第一个为1的bit（将该位的1置为0）](#%E5%88%A0%E9%99%A4%E4%BB%8E%E5%8F%B3%E8%BE%B9%E8%B5%B7%E7%AC%AC%E4%B8%80%E4%B8%AA%E4%B8%BA1%E7%9A%84bit%E5%B0%86%E8%AF%A5%E4%BD%8D%E7%9A%841%E7%BD%AE%E4%B8%BA0)
    - [判断一个数是否是2的幂次方](#%E5%88%A4%E6%96%AD%E4%B8%80%E4%B8%AA%E6%95%B0%E6%98%AF%E5%90%A6%E6%98%AF2%E7%9A%84%E5%B9%82%E6%AC%A1%E6%96%B9)
    - [判断一个数是否是4的幂次方](#%E5%88%A4%E6%96%AD%E4%B8%80%E4%B8%AA%E6%95%B0%E6%98%AF%E5%90%A6%E6%98%AF4%E7%9A%84%E5%B9%82%E6%AC%A1%E6%96%B9)
    - [计算2个数的和，递归方法](#%E8%AE%A1%E7%AE%972%E4%B8%AA%E6%95%B0%E7%9A%84%E5%92%8C%E9%80%92%E5%BD%92%E6%96%B9%E6%B3%95)
    - [计算2个数的差，递归方法](#%E8%AE%A1%E7%AE%972%E4%B8%AA%E6%95%B0%E7%9A%84%E5%B7%AE%E9%80%92%E5%BD%92%E6%96%B9%E6%B3%95)
    - [计算2个数的和，循环方法](#%E8%AE%A1%E7%AE%972%E4%B8%AA%E6%95%B0%E7%9A%84%E5%92%8C%E5%BE%AA%E7%8E%AF%E6%96%B9%E6%B3%95)
    - [找到丢失的数字,与相同的数异或两次后为0](#%E6%89%BE%E5%88%B0%E4%B8%A2%E5%A4%B1%E7%9A%84%E6%95%B0%E5%AD%97%E4%B8%8E%E7%9B%B8%E5%90%8C%E7%9A%84%E6%95%B0%E5%BC%82%E6%88%96%E4%B8%A4%E6%AC%A1%E5%90%8E%E4%B8%BA0)
    - [找到最高的一位数](#%E6%89%BE%E5%88%B0%E6%9C%80%E9%AB%98%E7%9A%84%E4%B8%80%E4%BD%8D%E6%95%B0)
    - [反转二进制位](#%E5%8F%8D%E8%BD%AC%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%BD%8D)
    - [找到从右边起，第一个为1的位，其余位置0](#%E6%89%BE%E5%88%B0%E4%BB%8E%E5%8F%B3%E8%BE%B9%E8%B5%B7%E7%AC%AC%E4%B8%80%E4%B8%AA%E4%B8%BA1%E7%9A%84%E4%BD%8D%E5%85%B6%E4%BD%99%E4%BD%8D%E7%BD%AE0)
    - [范围[m,n]之间所有数字与的结果](#%E8%8C%83%E5%9B%B4mn%E4%B9%8B%E9%97%B4%E6%89%80%E6%9C%89%E6%95%B0%E5%AD%97%E4%B8%8E%E7%9A%84%E7%BB%93%E6%9E%9C)

<!-- /TOC -->

[关于一切位操作的魔法 上中下](https://zhuanlan.zhihu.com/p/37175153)

# 特殊数字的16进制与二级制对应关系

```
0xaaaaaaaa = 10101010101010101010101010101010	(偶数位为1，奇数位为0）
0x55555555 = 1010101010101010101010101010101 	(偶数位为0，奇数位为1）
0x33333333 = 110011001100110011001100110011 	(1和0每隔两位交替出现)
0xcccccccc = 11001100110011001100110011001100 (0和1每隔两位交替出现)
0x0f0f0f0f = 00001111000011110000111100001111 (1和0每隔四位交替出现)
0xf0f0f0f0 = 11110000111100001111000011110000 (0和1每隔四位交替出现)
利用上述具有特殊二进制的整数，可以很方便进行位操作，而且该整数的十六进制形式比较好记，也不用写那么多的0，1。
```

# 二进制运算

## 特殊的取余操作

如果除数是2的幂次方，则等价于其除数减一的与操作。

也就是说hash % length == hash & (length - 1)的前提是length 是 2的n次方，并且采用二进制位操作&，相对于%能够提高运算效率，这就解释了hashmap的长度为什么是2的幂次方。

```c++
普通的求余运算为:  n % m，优化之后为n & (m - 1)。
public static int getMod(int n, int m) {
	return n & (m-1);
}
```

## 给定数字的二进制表示中1出现的个数

每次n&(n-1)操作都是将n最末尾的1反转为0，因此反转个数即为1的个数。

```c++
public static int count_one(int n) {
    int count = 0;
    while (n > 0) {
        // n&(n-1)作用是消除最低位的1，如二级制 111010&111001=111000
        n = n & (n - 1);
        count++;
    }
    return count;
}
```

## 将数字n的第bit位 置1

```c++
public static int resetBit_1(int n, int bit) {
    return n |= 1 << bit;
}
```

## 将数字n的第bit位 置0

```c++
public static int resetBit_0(int n, int bit) {
    return n &= ~(1 << bit);
}
```

## 数字n的第bit位 是否为0

```c++
public static boolean isBit0(int n, int bit) {
    return (n & (1 << bit)) != 0;
}
```

## 删除从右边起第一个为1的bit（将该位的1置为0）

```c++
public static int resetLowBit1To0(int n) {
    return n & (n - 1);
}
```

## 判断一个数是否是2的幂次方

这个数用二进制数表示时，只有一位为1。

```c++
public static boolean isPower(int n) {
    if ((n & (n - 1)) == 0)
        return true;
    else
        return false;
}
```

## 判断一个数是否是4的幂次方

这个数用二进制数表示时，**只有一位为1并且只可能出现在偶数位置**。

```c++
public static boolean isPowerOfFour(int n) {
   return ((n & (n - 1)) == 0) && ((n & 0x55555555) != 0);
   }
```

## 计算2个数的和，递归方法

```c++
public static int getSum(int a, int b) {
    return b == 0 ? a : getSum(a ^ b, (a & b) << 1);
}
```

## 计算2个数的差，递归方法

```c++
public static int getSubstract(int a, int b) {
    return b == 0 ? a : getSubstract(a ^ b, (~a & b) << 1);
}
```

## 计算2个数的和，循环方法

让我们以2+3为例来看一下： 0010（2），0011（3），首先看最右边的第一位，0+1为1，不进位，接着1+1=2，要进位。

我们如何判断相加的两个bit只有一个1？答案是使用异或操作。

我们如何判断相加的两个bit为两个1？答案是使用与操作。

因此 a&b的结果使得所有该进位的位置为1，a^b的结果使得所有该进位的位置0，不该进位的位置为其应该有的数。在进行初步的计算之后，我们需要把该进位的位置加上，因此进位之后，是在其前面的bit位加1，因此，需要将b左移1位，然后与初步计算结果相加，也就是我们递归方法的核心。

说说为什么最后b会变成0： 首先，carry <<1一定会使得carry中多一个0，因为左移之后最右边的位置一定为0，但是其前面可能舍弃了一个1，因此carry<<1使得carry的bit位的0的个数逐渐增加。其次，carry = a & b 这个使得b中的0得以保存，因为0 & 任何数都为0 因此，这两个条件使得最后b一定为0.同理，两个数相减也是一样的道理。首先a^b得到bit位上位数相同的位置全部为0，不同的位置为1，因为0-0=0，1-1=0；其次，~a&b得到需要借位的bit位，因此只有0-1需要借位，1-0不需要借位，因此~a & b刚好符合。

```c++
public static int getSum(int a, int b) {
    if (a == 0) {
        return b;
    }
    if (b == 0) {
        return a;
    }
    int carry = 0;
    while (b != 0) {
        // If both bits are 1, we set the bit to the left (<<1) to 1 -- this is the
        // carry step
        carry = (a & b) << 1;
        // If both bits are 1, this will give us 0 (we will have a carry from the step
        // above)
        // If only 1 bit is 1, this will give us 1 (there is nothing to carry)
        a = a ^ b;
        b = carry;
    }
return a;
}
```

## 找到丢失的数字,与相同的数异或两次后为0

一个正常数组包括0,1,2,3,4,5…n-1，但是现在这个数组中少了一个数，求这个数是多少？

例如：[0,1,3]输出结果为2。

```c++
public static int missingNumber(int[] nums) {
    int ret = 0;
    for (int i = 0; i < nums.length; ++i) {
        ret ^= i;
        ret ^= nums[i];
    }
    return ret ^= nums.length;
}
```

## 找到最高的一位数

```c++
public static int higestOneBit(int i) {
    i |= i >> 1;
    i |= i >> 2;
    i |= i >> 4;
    i |= i >> 8;
    i |= i >> 16;
    return (i + 1) >> 1;
}
```

## 反转二进制位

```c++
/**
 * 反转二进制位 翻转的顺序表示：abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
 *
 * @param n
 * @return
   */
   public static int reverseBit(int n) {
   n = (n >> 16) | (n << 16);
   n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
   n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
   n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
   n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
   return n;
   }
```

```c++
/**
 * 反转二进制位
 * 该解法的主要思路是：一个32位的mask，并且其32位中只有一个位为1，开始时，使其置1位位于最左端，
 * 并依次向最右移动，同时，从最右端开始检测n，如果n的对应位为1，则将结果或上mask。
 */
   public static int reverseBits(int n) {
   int mask = 1 << 31, res = 0;
   for (int i = 0; i < 32; ++i) {
   	if ((n & 1) != 0)
   		res |= mask;
   	mask >>= 1;
   	n >>= 1;
   }
   return res;
   }
```


## 找到从右边起，第一个为1的位，其余位置0

注：主要利用补码 = 反码 + 1

```c++
public static int getFirstOneFromRight(int n) {
    return n &= (-n);
}
```

## 范围[m,n]之间所有数字与的结果

多个数字相与，只要其中有一个数字为0结果就是0，而且，我们知道在数字递增的过程中，低位的数字总是在不断地变化，因此，我们只需要找到m与n相同的高位数字就行。

例如,5,6,7的二进制分别为：101       110       111，全部一样的部分为第三位，都为1，因此最后输出的结果为4。

```c++
public static int rangeBitwiseAnd(int m, int n) {
    int i = 0;
    while (m != n) {
        m >>= 1;
        n >>= 1;
        ++i;
    }
    return (m << i);
}
```

