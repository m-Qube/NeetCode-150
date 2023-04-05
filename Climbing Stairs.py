class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l1 = [1, 2]
        for i in range(2, n+1):
            l1.append(l1[i-1] + l1[i-2])
        return l1[n-1] 
