class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        total = len(nums1) + len(nums2) 
        half = total // 2
        
        if len(B) < len(A):
            A,B= B,A

        l = 0 
        r = len(A) - 1
        while True:
            i = (l+r)//2
            j = half - i - 2

            lA = A[i] if i >= 0 else float("-inf")
            rA = A[i+1] if i + 1 < len(A) else float("inf") 
            lB = B[j] if j >= 0 else float("-inf")
            rB = B[j+1] if j + 1 < len(B)  else float("inf") 
            if lA <= rB and rA >= lB:
                if total % 2:
                    return min(rA,rB)
                return (max(lA,lB) + min(rA,rB)) / 2
            elif lA > rB:
                r = i - 1
            else:
                l = i + 1
       
