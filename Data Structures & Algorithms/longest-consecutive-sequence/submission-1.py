class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#convert to set for removing duplicates
        num_set = set(nums)
#set longest 
        longest = 0
#loop through the nums array
        for num in num_set:

#find the start
            if num-1 not in num_set:
                
#assign current and length
                current = num
                length = 1
#walk ahead
                while current+1 in num_set:
                    current +=1
                    length += 1
#keep the longest sequence
                longest = max(longest, length)
        return longest