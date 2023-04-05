class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        minl, maxl = 0, 0
        for i in s:
            if i == '(':
                minl+=1
                maxl+=1
            elif i == ')':
                minl-=1
                maxl-=1
            else:
                minl-=1
                maxl+=1
            if minl<0:
                minl=0
            if maxl<0:
                return False
        return minl==0
