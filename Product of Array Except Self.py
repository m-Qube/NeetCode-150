class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1 for i in range(len(nums))]
        pre = 1
        for i in range(len(nums)):
            ans[i] = pre
            pre *= nums[i]

        post = 1
        for i in reversed(range(len(nums))):
            ans[i] *= post
            post *= nums[i]

        return ans
