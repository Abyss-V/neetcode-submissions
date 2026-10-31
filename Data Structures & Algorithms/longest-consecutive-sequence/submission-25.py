class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)

        m = 0
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] - 1 in seq:
                i+=1
          
            if i == len(nums):
                break

            mx = 1
            num = nums[i] + 1
            while num in seq:
                num += 1
                mx += 1 
        
            m = max(m,mx)
        
            i += 1
        return m


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         seq = {}
#         for i,n in enumerate(nums):
#             if n in seq:
#                 continue
#             seq[n] = n
#         path = {}
#         m = 0
#         mx = 0
#         i = 0
#         while i < len(nums):
#             if nums[i] + 1  in seq:
#                 path[nums[i]] = seq[nums[i] + 1]
#             else:
#                 path[nums[i]] = None
#             i += 1
#         for k in path:
#             m = 1
#             d = path[k]
#             while d:
#                 d = path[d]
#                 m += 1
#             mx = max(m,mx)

#         return mx
