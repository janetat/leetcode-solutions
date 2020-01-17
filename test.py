class Solution:
    def nextGreaterElement(self, nums1, nums2):
        cache = {}
        stack = []

        for n in nums2:
            while stack and n > stack[-1]:
                cache[stack.pop()] = n
            stack.append(n)

        # return [cache[n] if n in cache else -1 for n in nums1]
        return [cache[n] for n in nums1]