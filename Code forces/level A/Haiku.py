inp1 = input()
inp2 = input()
inp3 = input()
count1 = 0 
count2 =0
count3 =0
for i in range (0,len(inp1)):
    if(inp1[i] == 'a' or inp1[i] == 'e' or inp1[i] == 'i' or inp1[i] == 'o' or inp1[i] == 'u'):
        count1 = count1 + 1

for i in range (0,len(inp2)):
    if(inp2[i] == 'a' or inp2[i] == 'e' or inp2[i] == 'i' or inp2[i] == 'o' or inp2[i] == 'u'):
        count2 = count2 + 1

for i in range (0,len(inp3)):
    if(inp3[i] == 'a' or inp3[i] == 'e' or inp3[i] == 'i' or inp3[i] == 'o' or inp3[i] == 'u'):
        count3 = count3 + 1
if(count1 ==5 & count2 ==7 & count3 ==5):
    print("YES")
else:
    print("NO")
