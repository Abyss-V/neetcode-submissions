class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        if strs == [""]:
            return " "
        for s in strs:
            res.append(s.encode('utf-8').hex())
        res = "-".join(res)
        return res
    def decode(self, s: str) -> List[str]:

        if s == " ":
            return [""]
        if s == "":
            return []
        r = s.split("-")
        res = []
        for c in r:
            res.append(bytes.fromhex(c).decode('utf-8'))
        return res