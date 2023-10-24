class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score) + 1)))
        place = sorted(score, reverse = True)
        d = dict(zip(place, rank))

        return [d.get(s) for s in score]