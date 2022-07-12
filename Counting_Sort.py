def count_sort(arr):
    max_element = int(max(arr))
    min_Element = int(min(arr))
    count_Array = [0 for _ in range(min_Element,max_element+1)]
    output_Array = [0 for _ in range(len(arr))]
    #store count of each number
    for i in range(0,len(arr)):
        count_Array[arr[i]-min_Element]+=1

    for i in range(1,len(count_Array)):
        count_Array[i] =(count_Array[i-1]+count_Array[i])
    for i in range(len(arr)-1,-1,-1):
        output_Array[count_Array[arr[i]-min_Element]-1] = arr[i]
        count_Array[arr[i]-min_Element]-= 1
    for i in range(0,len(arr)):
        arr[i] = output_Array[i]
    return arr


    print(count_Array)


if __name__ =="__main__":
    arr = [-5, -10,-10, 0, -3, 8, 5, -1, 10]
    ans = count_sort(arr)
    print("Sorted character array is " + str(ans))