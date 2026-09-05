class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        result = sorted(count, key = lambda num: count[num], reverse = True) # key = lambda num: count[num] --> it says for each "num" use its frequency (count[num]) as the sorting key (key =) lambda is just a function to denote this
        return result[:k]