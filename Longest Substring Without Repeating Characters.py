class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        l1=[]
        l2=[]
        for i in range(len(s)):
            for k in range(i,len(s)):
                if s[k] not in l1:
                    l1.append(s[k])
                else:
                    l2.append(len(l1))
                    l1=[]
                    break
        return max(l2)
