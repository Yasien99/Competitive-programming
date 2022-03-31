import statistics
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort() 
        del salary[0]
        del salary[-1]
        return statistics.mean(salary)