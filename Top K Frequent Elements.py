class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict1 = {}
        ans=[]
        for i in set(nums):
            dict1[i] = nums.count(i)
            sorted_ = sorted(dict1.items(), key = lambda x: x[1], reverse=True)
        for i in sorted_[:k]:
            ans.append(i[0])
        return ans
