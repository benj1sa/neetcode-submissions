class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            starg = target - n
            l = i + 1
            r = len(numbers) - 1
            res = -1
            while l <= r:
                mid = (r - l) // 2 + l
                if numbers[mid] == starg:
                    return [i + 1, mid + 1]
                elif numbers[mid] < starg:
                    l = mid + 1
                else:
                    r = mid - 1
        return []