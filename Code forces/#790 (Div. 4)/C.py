alphabet = {
        'a' : 1, 
        'b' : 2, 
        'c' : 3, 
        'd' : 4, 
        'e' : 5, 
        'f' : 6, 
        'g' : 7, 
        'h' : 8, 
        'i' : 9, 
        'j' : 10, 
        'k' : 11, 
        'l' : 12, 
        'm' : 13, 
        'n' : 14, 
        'o' : 15, 
        'p' : 16, 
        'q' : 17, 
        'r' : 18, 
        's' : 19, 
        't' : 20, 
        'u' : 21, 
        'v' : 22, 
        'w' : 23, 
        'x' : 24, 
        'y' : 25, 
        'z' : 26
    }

def check(st1 , st2):
    diff = 0
    for x in range(len(st1)):
        if(st1[x] != st2[x]):
            diff = diff + abs(alphabet[st1[x]] - alphabet[st2[x]])
    return diff

t = int(input())
for q in range(t):
    dif = []
    str = []
    n ,m = input ().split(" ")
    n = int(n) #num of strings
    m = int(m)  #their length 
    for i in range(n):
        str.append(input())
    for k in range (n):
        for j in range(k+1,n):
            dif.append(check(str[k],str[j]))
    print(min(dif))