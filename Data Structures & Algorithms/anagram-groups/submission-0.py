class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = {}

        for word in strs:
            sig = "".join(sorted(word))

            if sig in store:
                store[sig].append(word)
            else:
                store[sig] = [word]
                
        return list(store.values())





        



        