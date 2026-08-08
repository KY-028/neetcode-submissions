class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Idea: start with 2 partitions then adjust
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r) // 2
            j = half - i - 2  # half size - A elements - 2 indices
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')

            # If this is the right partitioning for half:
            # 1) the biggest in A left half <= smallest of B right half
            # 2) the biggest in B left half <= smallest of A right half
            if Aleft <= Bright and Bleft <= Aright:
                # found sol
                if total % 2:
                    return min(Aright, Bright) #because left half contains 1 less element
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # otherwise if A left half is too big (more elements should be in B)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        