
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(s+":;")
        return "".join(s for s in res)
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = s.split(":;")
        res = res[:-1]
        return res

# other way of solving the problem