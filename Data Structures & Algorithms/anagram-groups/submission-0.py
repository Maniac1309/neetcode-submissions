class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Create a dictionary.
    # For each string:
    #     convert it to a list
    #     sort it
    #     convert it to a tuple
    #     use that tuple as the key
    # If key exists, append the string.
    # Otherwise, create a new list.
    # Return the dictionary's values.
        groups = {}
        for s in strs:
            chars = list(s)
            chars.sort()
            key = tuple(chars)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())