class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 in nset:
                continue
            n = nums[i]
            while n in nset:
                n += 1
            longest = max(longest, n - nums[i])
        return longest