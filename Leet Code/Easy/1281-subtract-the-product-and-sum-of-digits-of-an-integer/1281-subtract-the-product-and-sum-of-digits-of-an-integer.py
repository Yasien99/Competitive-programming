class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        count = 0
        sum_dig = 0
        product = 1
        while(n != 0):
            sum_dig = sum_dig + n%10
            product = product * (n%10)
            n = int(n // 10)
        return(product - sum_dig)