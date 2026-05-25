class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## hashmap: key (sorted string), value (list of original strings)
        ## iterate through the array adding to the hashmap

        anagramStore = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagramStore[sortedWord].append(word)
        
        return list(anagramStore.values())