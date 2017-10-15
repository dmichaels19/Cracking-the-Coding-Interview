class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_sub = 0
        start_pos = 0
        unique_chars = set()
        for i, char in enumerate(s):
            if char not in unique_chars:
                longest_sub = max(longest_sub, i - start_pos + 1)
            else:
                while(start_pos <= i and char in unique_chars):
                    unique_chars.remove(s[start_pos])
                    start_pos += 1
            unique_chars.add(char)
        return longest_sub