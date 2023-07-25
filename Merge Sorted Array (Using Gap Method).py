class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        def swap_if_greater(arr1, arr2, ind1, ind2):
            if arr1[ind1] > arr2[ind2]:
                arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

        del nums1[m:m + n]
        nums1.sort()
        len1 = m + n
        gap = (len1 / 2) + (len1 % 2)

        while gap > 0:
            lft = 0
            rgt = lft + gap
            while rgt < len1:
                if lft < m and rgt >= m:    #nums1 and nums2
                    swap_if_greater(nums1, nums2, lft, rgt-m)
                    # print(nums1, nums2)
                elif lft >= m:             #nums2 and nums2
                    swap_if_greater(nums2, nums2, lft - m, rgt - m)
                    # print(nums1, nums2)
                else:                      #nums1 and nums1
                    swap_if_greater(nums1, nums1, lft, rgt)
                    # print(nums1, nums2)
                lft += 1
                rgt += 1
            if gap == 1:
                break
            gap = (gap / 2) + (gap % 2)
        nums1 += nums2
        nums2 = []
