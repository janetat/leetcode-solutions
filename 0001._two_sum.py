class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for index, num in enumerate(nums):
            if target - num in hash_table:
                answers = [index, hash_table[target - num]]
                return answers
            else:
                hash_table[num] = index


