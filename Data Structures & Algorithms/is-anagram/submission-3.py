class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.lower()
        t.lower()
        if ( sorted(s) == sorted(t)):
            return True
        else:
            return False