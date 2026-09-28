class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ncount = {}
        for n in nums:
            ncount[n] = 1 + ncount.get(n, 0)
        
        freqs = [[] for _ in range(len(nums) + 1)]
        for n in ncount:
            freqs[ncount[n]].append(n)

        kfreq = []
        for i in range(len(freqs) - 1, -1, -1):
            for elem in freqs[i]:
                kfreq.append(elem)
                if len(kfreq) == k:
                    return kfreq
        return kfreq