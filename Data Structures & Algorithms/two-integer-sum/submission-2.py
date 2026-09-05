class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums): #enumerate gives both the index and the value
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i