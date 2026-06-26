class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        t is anagram of s if t has all characters as in s (including repeated ones)
        but they can be rearranged in any way
        """
        stat_s = {}
        stat_t = {}
        if len(s) != len(t):
            return False
        
        for ch_s, ch_t in zip(s, t):
            print(ch_s, ch_t)
            if ch_s not in stat_s:
                stat_s[ch_s] = 1
            else:
                stat_s[ch_s] += 1
            if ch_t not in stat_t:
                stat_t[ch_t] = 1
            else:
                stat_t[ch_t] += 1

        if stat_s == stat_t:
            return True
        else:
            return False    
        
        