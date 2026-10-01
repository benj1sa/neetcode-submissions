class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i, n in enumerate(nums):
            if target - n in nmap:
                return [nmap[target - n], i]
            nmap[n] = i
        return []