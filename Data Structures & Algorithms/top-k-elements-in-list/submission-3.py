class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        output = []
        for key,v in freq.items():
            output.append((key,v))

        return [e[0] for e in sorted(output,key=lambda x:x[1],reverse=True)][:k]