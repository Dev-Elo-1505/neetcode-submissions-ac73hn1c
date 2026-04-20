class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for n, f in counter.items():
            freq[f].append(n)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res