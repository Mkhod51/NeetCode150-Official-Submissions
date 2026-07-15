class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = [str(len(n)) for n in strs]
        lengthsStr = "-".join(lengths) + "#"
        strs.insert(0, lengthsStr)
        return "".join(strs)


    def decode(self, s: str) -> List[str]:
        counts, strs = s.split("#", 1)
        if counts == "":
            return []

        retStrs = []
        pos = 0
        for c in counts.split("-"):
            retStrs.append(strs[pos:pos+int(c)])
            pos = pos + int(c)
        
        return retStrs
