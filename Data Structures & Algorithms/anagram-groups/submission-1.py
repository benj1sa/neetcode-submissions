class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            chars = [0] * 26
            for c in string:
                chars[ord(c) - ord('a')] += 1
            key = ",".join(str(n) for n in chars)

            if key not in groups:
                groups[key] = []
            groups[key].append(string)
        
        return list(groups.values())