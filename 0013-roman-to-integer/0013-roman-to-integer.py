class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={'I': 1,'IV': 4,  'V': 5, 'X': 10, 'IX': 9, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        answer=0
        
        for i in range(len(s)-1, -1, -1):
            num=dic[s[i]]
            if 4 * num < answer:
                answer -= num
            else:
                answer+=num
        return answer
        