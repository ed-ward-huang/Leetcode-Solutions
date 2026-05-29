class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        res = 0
        
        left = 0
        maxFrequency = 0
        for right in range(len(s)):
            store[s[right]] = store.get(s[right], 0) + 1
            maxFrequency = max(maxFrequency, store[s[right]])

            while (right - left + 1) - maxFrequency > k:
                store[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res