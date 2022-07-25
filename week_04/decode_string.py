
"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def _decodeS(s ,start ,end):
            i ,ans =start ,""
            while i< end:
                d = i
                while i < end and s[i].isdigit(): i = i + 1
                repeat = int(s[d:i]) if i > d else 1
                j, c = i, 0
                if s[i] != '[':
                    while j < end and s[j].isalpha(): j = j + 1
                    return ans + s[i:j] + _decodeS(s, j, end)
                while j < end:
                    if s[j] == '[':
                        c = c + 1
                    elif s[j] == ']':
                        c = c - 1
                    if c == 0: break
                    j = j + 1
                ans = ans + _decodeS(s, i + 1, j) * repeat
                i = j + 1
            return ans

        return _decodeS(s, 0, len(s))