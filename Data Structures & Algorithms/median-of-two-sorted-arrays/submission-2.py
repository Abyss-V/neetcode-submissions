class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        n.sort()
        if len(n) % 2 == 0:
            return (n[(len(n)-1) //2] + n[((len(n)-1) //2)+1]) / 2

        return n[(len(n)-1) //2]

# time: O(nlogn) ; space:O(n+m)