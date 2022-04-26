n = int(input())
input_x = []
while(n):
    temp = int(input())
    input_x.append(temp)
    n = n -1

for i in range (0,len(input_x)):
    if(input_x[i] >= 1900):
        print("Division 1")
    elif(input_x[i] >= 1600):
        print("Division 2")
    elif(input_x[i] >= 1400):
        print("Division 3")
    elif(input_x[i] <= 1399):
        print("Division 4")
        