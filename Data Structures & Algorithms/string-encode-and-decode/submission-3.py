class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "$" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        lenbuff = ""
        while i < len(s):
            if s[i] == "$":
                length = int(lenbuff)
                decoded.append(s[i + 1:i + length + 1])
                lenbuff = ""
                i += length + 1
            else:
                lenbuff += s[i]
                i += 1
        return decoded