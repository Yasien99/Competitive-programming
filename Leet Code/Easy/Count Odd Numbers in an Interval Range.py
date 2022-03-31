import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) / 2
        #if both nums are odd add 1 to the count 
        if (low%2 != 0) and (high%2 != 0):
            count+=1
        count = math.ceil(count)
        return count