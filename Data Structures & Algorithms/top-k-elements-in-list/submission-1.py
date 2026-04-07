class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for count in nums:
            if count in freq_dict:
                freq_dict[count] += 1
            else:
                freq_dict[count] = 1

        freq_list = []
        for num, freq in freq_dict.items():
            freq_list.append((freq, num))

        freq_list.sort(reverse=True)

        result = []
        for i in range(k):
            freq, num = freq_list[i]
            result.append(num)
        
        return result
        