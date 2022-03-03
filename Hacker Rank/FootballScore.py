def binarySearchCount(arr, n, key):
    left = 0
    right = n
    mid = 0
    while (left < right):
        mid = (right + left)//2
        if (arr[mid] == key):
            while (mid + 1<n and arr[mid + 1] == key):
                 mid+= 1
            break
        elif (arr[mid] > key):
            right = mid
        else:
            left = mid + 1
    while (mid > -1 and  arr[mid] > key):
        mid-= 1
    return mid + 1
result = []

def counts(teamA,teamB):
    count = 0
    j=0
    teamA.sort()
    for i in range(0,len(teamB)): 
        count = binarySearchCount(teamA,len(teamA),teamB[i])
        result.append(count)
        count = 0
        j = 0
    return(result)

#teams test goals
teamA = [1,2,3]
teamB = [2,4]

#output
print(counts(teamA,teamB))

