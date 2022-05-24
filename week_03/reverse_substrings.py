
'''
You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.
Example 1:
Input: s = "(abcd)"
Output: "dcba"
Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
Constraints:
1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
'''
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        revers=''
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                tmp=s[stack[-1]:i +1]
                s=s[:stack[-1]] + tmp[::-1] + s[i+1:]
                stack.pop()
        for i in range(len(s)):
            if s[i]!=')' and s[i]!='(':
                revers+=s[i]
        return revers

        # for el in s:
        #     if el!=')':
        #         stack.append(el)
        #         print(stack)
        #     elif el==')':
        #         while stack:
        #             new=stack.pop()
        #             if new=='(':
        #                 break
        #             else:
        #                 revers+=new
        #
        # return revers

def main():
    sol = Solution()
    st= '(abcd)'
    s = "(u(love)i)"
    print(sol.reverseParentheses(s))


main()


