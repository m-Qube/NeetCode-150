class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        n = len(nums)
        k = k % n
        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)
