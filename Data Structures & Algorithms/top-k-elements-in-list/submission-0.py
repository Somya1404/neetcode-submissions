class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for var in nums:
            count[var] = count.get(var,0) + 1
        sorted_nums = sorted(count , key = count.get , reverse = True)
        return sorted_nums[:k]    