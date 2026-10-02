class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        freq = [[] for _ in range(len(nums) + 1)]
        for n, count in counts.items():
            freq[count].append(n)
        elements = []
        for i in range(len(nums), -1, -1):
            for elem in freq[i]:
                elements.append(elem)
                if len(elements) == k:
                    return elements
        return []