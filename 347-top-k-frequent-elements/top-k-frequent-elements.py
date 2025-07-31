class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for x in nums:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1
        
        sorted_keys = sorted(counter, key=counter.get, reverse=True)
        return sorted_keys[:k]
        