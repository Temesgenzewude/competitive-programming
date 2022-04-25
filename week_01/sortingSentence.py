class Solution:
    def sortSentence(self, s):
        lst = s.split()
        result = ""

        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if int(lst[i][-1]) > int(lst[j][-1]):
                    lst[i], lst[j] = lst[j], lst[i]
        for a in lst:
            a = a[:-1]
            result += a
            result += " "

        return result.strip()


def main():
    s = "is2 sentence4 This1 a3"
    result = Solution().sortSentence(s)
    print(result)


main()
