class Solution:
    def isPalindrome(self, s: str) -> bool:
        combine=''

        for c in s:
            if c.isalnum():
                combine +=c.lower()

        left=0
        right=len(combine)-1

        while left<right:
            if combine[left] != combine[right]:
                return False
            left +=1
            right-=1
        return True
            

        