# Python  program for recursive binary search.
import timeit
def binary_search(arr,low,high,element):
    if high>=low:
        mid = (low+high)//2


        if arr[mid]==element:
            return mid
        elif arr[mid]>element:
            return binary_search(arr,low,mid-1,element)
        else:
            return binary_search(arr,mid+1,high,element)
    else:
        return -1
if __name__ == '__main__':
    arr = list(range(0,100000+2,2))
    print(f"len {len(arr)}")

    inp = sorted(arr)
    low = 0
    high=len(inp)
    # print(inp)
    x = 100000
    print(binary_search(inp,low,high,x))
    print(timeit.timeit())
    print("Recuresive")

# Iterative Binary Search Function
def binary_search1(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <=high:
        mid = (high+low)//2
        if arr[mid]<x:
            low = mid+1
        elif arr[mid]>x:
            high = mid-1
        else:
            return mid
    return -1
if __name__ =='__main__':
    # arr = [2,3,4,56,25,3,5]
    arr = list(range(0,100000+2,2))
    arr = sorted(arr)
    x = 100000
    print(binary_search1(arr,x))
    print("iterative")
    print(timeit.timeit())



