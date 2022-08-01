def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j!= length:
            buckets[j].append(alist[i])
        else:buckets[length-1].append((alist[i]))

    for i in range(length):
        insertionSort(buckets[i])
    result = []
    for i in range(length):
        result+=buckets[i]
    return result
def insertionSort(alist):
    for i in range(1,len(alist)):
        key = alist[i]
        j=i-1
        while(j>=0 and key<alist[j]):
            alist[j+1] =alist[j]
            j=j-1
        alist[j+1] = key
arr = [0.78,.17,.39,.72]
result = bucketSort(arr)
print(result)