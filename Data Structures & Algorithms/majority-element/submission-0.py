class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}

        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1

        maj_element = None
        maj_freq = 0

        for i in frequency:
            if frequency[i] > maj_freq:
                maj_freq = frequency[i]
                maj_element = i
        return maj_element


        