from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        
        for n in nums:
            freq[n] += 1
        heap = [(freq[key], key) for key in freq]
        heapq.heapify(heap);

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [key for v, key in heap]