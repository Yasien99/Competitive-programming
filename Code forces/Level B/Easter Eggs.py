
eggs = input()
eggs = int(eggs)
ans= "ROYGBIV"; 
while(eggs >= 7 & eggs <= 100):
    #start from the end of ans and then add the 4th last element from your pos
    for i in range(len(ans),eggs):
        ans += ans[i - 4]
    print(ans,end="")
    break
