class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""

        if strs == []:
            return " "
        for i, s  in enumerate(strs):
        
                strs[i] = s.encode('utf-8').hex()
        r = "-".join(strs)

        return r
    def decode(self, s: str) -> List[str]:
     
        if s == " ":
            return []
        d = s.split("-")
        res = []
        for st in d:
            res.append(bytes.fromhex(st).decode('utf-8'))
        return res