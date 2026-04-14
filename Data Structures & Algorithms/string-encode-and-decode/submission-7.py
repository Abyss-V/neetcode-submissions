
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s
            res += ":;"
        return res

        return res
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = s.split(":;")
        res = res[:-1]
        result = []
        for a in res:
            result.append(a)
        return result

# other way of solving the problem