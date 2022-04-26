def pairwise (digits):

    max1 = max(digits)  
    digits.remove(max1)
    max2 = max(digits)
        
    return max1 * max2

n= int(input())
for i in range(n):
    digits = [int(item) for item in input().split()]
    print(pairwise(digits))

