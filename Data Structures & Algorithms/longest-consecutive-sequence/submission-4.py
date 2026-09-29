class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0
        for n in nums:
            if n - 1 in nset:
                continue
            else:
                i = n
                while i in nset:
                    i += 1
                longest = max(longest, i - n)
        
        return longest