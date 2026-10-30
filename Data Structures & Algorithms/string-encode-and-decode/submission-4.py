class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        if strs == []:
            return " "
        for i,s  in enumerate(strs):
            if i < len(strs) - 1:
                r += s.encode('utf-8').hex() + "-"
            else:
                r += s.encode('utf-8').hex()
        return r
    def decode(self, s: str) -> List[str]:
     
        if s == " ":
            return []
        d = s.split("-")
        res = []
        for st in d:
            res.append(bytes.fromhex(st).decode('utf-8'))
        return res