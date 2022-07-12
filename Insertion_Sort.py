class Insertion_Sort:
    def insertion_Sort(self,arr):
        for i in range(1,len(arr)):

            key = arr[i]
            j = i-1
            while j>=0 and key<arr[j]:
                arr[j+1] = arr[j]
                j -=1
            arr[j+1] = key
        return arr
if __name__ == '__main__':
    arr = [12,11,13,5,6]
    obj = Insertion_Sort()
    result = obj.insertion_Sort(arr)
    print(result)








































#
# def insertionSort1(alist):
#         for index in range(1,len(alist)):
#             key = alist[index]
#             j = index-1
#             while j>=0 and key>  alist[j]:
#                 alist[j+1] = alist[j]
#
#                 j-=1
#             alist[j+1] = key
#         return alist
# aarr = [4,2,3,1]
# print(insertionSort1(aarr))

