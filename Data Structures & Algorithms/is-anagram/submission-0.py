class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = {}
        for ch in s:
            res[ch] = True
        for ch in t:
            if ch not in res:
                return False
        return True
        