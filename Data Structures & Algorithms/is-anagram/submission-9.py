class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        result = {}

        for i in s:
            result[i] = result.get(i, 0) +1

        for i in t:
            if i not in result:
                return False

            result[i] -= 1
            if result[i] < 0:
                return False
        return True




        

        

        



