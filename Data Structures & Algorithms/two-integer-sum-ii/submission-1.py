class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            starg = target - n
            l = 0
            r = len(numbers) - 1
            res = -1
            while l <= r:
                mid = (r - l) // 2 + l
                if numbers[mid] == starg:
                    res = mid
                    break
                elif numbers[mid] < starg:
                    l = mid + 1
                else:
                    r = mid - 1
            if res >= 0 and i != res:
                return [i + 1, res + 1] if i + 1 < res + 1 else [res + 1, i + 1]
        return []