class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += s.encode().hex() + "-"
        return output
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        output = []
        for s in s.split("-")[:-1]:
                output.append(bytes.fromhex(s).decode())
        return output