"""
Option 1: merge the two list then perform binary search
Option 2: 

"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # make sure A is always the smaller list
        if len(B)< len(A):
            A, B = B, A
            
        l, r = 0 , len(A) - 1
        
        while True:
            i = (l + r) // 2 # index of A
            j = half - i - 2 # B, minus 2 because of the "off-by-one" error, for both i and j
            
            # Check for correct partition, also make sure to set as infinity if out of bound
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: # when Aleft is too big to the right
                r = i - 1
            else: #Bleft > Aright
                l = i + 1
                