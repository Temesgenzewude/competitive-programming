'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'{': '}', '[': ']', '(': ')'}
        if len(s) % 2 != 0:
            return False

        stack = []
        # for i in range(0, len(s) - 1, 2):
        #     if s[i] not in dic:
        #         return False
        #
        #     if dic[s[i]] != s[i + 1]:
        #         return False
        #
        # return True

        for b in s:
            if b in dic:
                stack.append(b)
            elif b==')':
                if not stack or stack.pop()!='(':
                    return False
            elif b=='}':
                if not stack or stack.pop()!='{':
                    return False
            elif b==']':
                if not stack or stack.pop()!='[':
                    return False
        return not stack


def main():
    sol = Solution()
    s1 = "()"
    s2 = "()[]{}"
    s3 = "([]"

    print(sol.isValid(s3))


main()
