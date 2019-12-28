class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # guarantees that nums2 is longer than nums1 by swapping the 2 
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        m,n = len(nums1), len(nums2)
        if n == 0: raise ValueError
            
       # i between 0 and len(nums1)
       # half_len is half of the combined lengths + 1 
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            # if i is too small
            if i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            # if i is too big
            elif i > 0 and nums2[j] < nums1[i-1]:
                imax = i - 1
            else: 
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0
        