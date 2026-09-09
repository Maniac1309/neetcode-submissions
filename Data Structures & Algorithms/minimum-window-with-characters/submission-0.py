class Solution:

    def minWindow(self, s: str, t: str) -> str:

        # required = frequency of each character that t needs
        required = {}

        for char in t:
            required[char] = required.get(char, 0) + 1

        # count = frequency of characters inside current window
        count = {}

        # Start of sliding window
        left = 0

        # Number of required character occurrences
        # currently satisfied by the window
        matched = 0

        # Smallest window length found so far
        min_length = float("inf")

        # Actual shortest substring
        result = ""

        # Expand window using right
        for right in range(len(s)):

            # Add current character to the window
            count[s[right]] = count.get(s[right], 0) + 1

            # If this character is required and
            # we haven't exceeded the required frequency,
            # we have matched one more character
            if s[right] in required and count[s[right]] <= required[s[right]]:
                matched += 1

            # Window contains everything required by t
            # Try to make it smaller
            while matched == len(t):

                # Save this window if it's the smallest so far
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left:right + 1]

                # Check whether removing s[left]
                # will make the window miss a required character
                if s[left] in required and count[s[left]] <= required[s[left]]:
                    matched -= 1

                # Remove left character from window
                count[s[left]] -= 1

                # Shrink window
                left += 1

        return result