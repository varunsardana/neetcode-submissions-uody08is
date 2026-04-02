class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        for i in range(len(strs[0])):      # loop through each character position
            for s in strs[1:]:             # check that character in every string
                if i >= len(s) or s[i] != strs[0][i]:
                    return prefix          # mismatch or string too short → stop
            prefix += strs[0][i]           # all strings matched → add to prefix
        
        return prefix

            

        