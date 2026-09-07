class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0
        for n in nums:
            if n-1 in nset:
                continue
            start = n
            while n in nset:
                n += 1
            longest = max(longest, n - start)
        return longest