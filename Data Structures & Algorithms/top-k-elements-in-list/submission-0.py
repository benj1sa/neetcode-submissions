class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        char_count = {}
        for n in nums:
            char_count[n] = char_count.get(n, 0) + 1

        freq = defaultdict(list)
        max_count = float('-inf')
        for n, count in char_count.items():
            max_count = max(count, max_count)
            freq[count].append(n)

        res = []
        for count in range(max_count, 0, -1):
            for n in freq[count]:
                res.append(n)
                if len(res) == k:
                    return res
        return []