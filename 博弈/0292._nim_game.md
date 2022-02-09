# Navigation

# Links
1. https://leetcode.com/problems/nim-game/
2. https://leetcode-cn.com/problems/nim-game/


# Solution 1 堆中石头的数量 n 不能被 4 整除
题目已假设每一步都是最优解。
```python
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n % 4) != 0
```