class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        number = num
        for i in range(t):
            number += 2
        return number