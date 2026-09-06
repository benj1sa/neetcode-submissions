class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "@" + s
        return encoded

    # "0123456789..."
    # "6@Design2@an9@algorithm" -> ["Design", "an", "algorithm"]

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        length = ""
        while i < len(s):
            if s[i] != "@":
                length += s[i]
                i += 1
            else:
                l = int(length)
                decoded.append(s[i+1:i+l+1])
                i += l + 1
                length = ""
        return decoded