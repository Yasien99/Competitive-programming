class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequency = Counter(tasks)
        rou = 0
        for freq in frequency.values():
            if freq == 1:
                return -1
            elif (freq-2) % 3 == 0:
                rou += (freq-2) // 3 + 1
            elif (freq - 4) % 3 == 0:
                rou += (freq - 4) // 3 +2
            elif freq % 3 == 0:
                rou += freq // 3
            else:
                rou += freq // 2
        return rou
        