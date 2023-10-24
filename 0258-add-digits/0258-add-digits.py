class Solution:
    def addDigits(self, num: int) -> int:
        if num >= 10:
            output = num // 10 + num % 10
            if output < 10:
                return output
            else:
                return self.addDigits(output)
        else:
            return num