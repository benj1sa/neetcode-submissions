class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "$" + s
        return encoded

    # 0123456789
    # 5$hello4$tree
    # len(s) = 13

    # decoded = []
    # i = 7
    # s[i] = $
    # buffer = "5"
    # slen = 5
    # s[i+1:i+1+slen] = 
    # s[2:] 

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        buffer = ""
        while i < len(s):
            if s[i] == "$":
                slen = int(buffer)
                decoded.append(s[i+1:i+1+slen])
                i += slen + 1
                buffer = ""
            else:
                buffer += s[i]
                i += 1
        return decoded