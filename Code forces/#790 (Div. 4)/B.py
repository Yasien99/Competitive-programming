t = int(input())
for i in range(t):
    candies  = 0
    n = int(input())
    digits = [int(num) for num in input().split(" ")]
    min_num =min(digits)
    for i in range(len(digits)):
        candies = candies + (digits[i] - min_num)
    print(candies)