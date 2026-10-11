class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for k in set(s):
            if s.count(k)!=t.count(k):
                return False
        return True
        