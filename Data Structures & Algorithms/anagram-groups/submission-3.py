class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            cmap = [0] * 26
            for c in s:
                cmap[ord('a') - ord(c)] += 1
            key = ""
            for i in cmap:
                key += str(i)
            groups[key].append(s)
        return list(groups.values())