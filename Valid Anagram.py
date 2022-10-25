class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sset=set(s)
        sdict={}
        tset=set(t)
        tdict={}
        for i in sset:
            sdict.update({i:s.count(i)})
        for i in tset:
            tdict.update({i:t.count(i)})
        return sdict==tdict