class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            string1 = sorted(s)
            string2 = sorted(t)
            if(string1 == string2):
                return True
            else:
                return False
        else:
            return False
