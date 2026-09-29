class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nmap = defaultdict(list)
        for i, n in enumerate(nums):
            nmap[n].append(i)
        n = len(nums)
        tset = set()
        for i in range(n):
            for j in range(i, n):
                target = -1*(nums[i] + nums[j])
                if target in nmap:
                    for k in nmap[target]:
                        if k != i and k != j and i != j:
                            tset.add(",".join(map(str, sorted([nums[i],nums[j],nums[k]]))))
                            break
        triplets = []
        for lstring in tset:
            intarr = [int(x) for x in lstring.split(",")]
            triplets.append(intarr)
        return triplets