t = int(input())
for i in range(t):
    digits = input()
    sum1 = int(digits[0]) + int(digits[1]) + int(digits[2])
    sum2 = int(digits[3]) + int(digits[4]) + int(digits[5])
    if(sum1 == sum2):
        print("Yes")
    else:
        print("No")
 