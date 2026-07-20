class Solution:
    def isAlphaNumeric(self, c):
        print(c)
        if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        """
            012345678
        "   tab a cat   "
        ptr1 = str[0], ptr2 = str[-1]
        moving left to right and right to left.
        ignore special chars on the way
        """
        s = s.replace(' ', '').lower()
        if len(s) <= 1:
            return True
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            print(p1, p2)
            while p1 < p2 and self.isAlphaNumeric(s[p1]) is False:
                p1 += 1
            while p2 > p1 and self.isAlphaNumeric(s[p2]) is False:
                p2 -= 1

            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        
        return True
        