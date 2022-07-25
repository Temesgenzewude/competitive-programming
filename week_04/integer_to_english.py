
"""
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:

0 <= num <= 231 - 1
"""


class Solution:
  def numberToWords(self, num: int) -> str:
    if num == 0:
      return "Zero"

    belowTwenty = ["",        "One",       "Two",      "Three",
                   "Four",    "Five",      "Six",      "Seven",
                   "Eight",   "Nine",      "Ten",      "Eleven",
                   "Twelve",  "Thirteen",  "Fourteen", "Fifteen",
                   "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["",      "Ten",   "Twenty",  "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def helper(num: int) -> str:
      if num < 20:
        s = belowTwenty[num]
      elif num < 100:
        s = tens[num // 10] + " " + belowTwenty[num % 10]
      elif num < 1000:
        s = helper(num // 100) + " Hundred " + helper(num % 100)
      elif num < 1000000:
        s = helper(num // 1000) + " Thousand " + helper(num % 1000)
      elif num < 1000000000:
        s = helper(num // 1000000) + " Million " + \
            helper(num % 1000000)
      else:
        s = helper(num // 1000000000) + " Billion " + \
            helper(num % 1000000000)

      return s.strip()

    return helper(num)