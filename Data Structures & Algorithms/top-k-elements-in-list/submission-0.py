from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        counts = Counter(nums)

        for key, freq in counts.items():
            heapq.heappush(h, (-freq, key))

        results = []

        for _ in range(k):
            freq, key = heapq.heappop(h)
            results.append(key)

        return results